package main

import (
	"fmt"
	"image"
	"image/color"
	"image/jpeg"
	"image/png"
	"log"
	"os"
	"sync"
	"time"
)

func processImage(img image.Image) image.Image {
	// Procesamiento: convertir a escala de grises (ejemplo simple)
	bounds := img.Bounds()
	grayImg := image.NewGray(bounds)
	for y := bounds.Min.Y; y < bounds.Max.Y; y++ {
		for x := bounds.Min.X; x < bounds.Max.X; x++ {
			oldColor := img.At(x, y)
			r, g, b, _ := oldColor.RGBA()
			// Promedio
			avg := uint8((r + g + b) / 3 >> 8)
			newColor := color.Gray{Y: avg}
			grayImg.Set(x, y, newColor)
		}
	}
	return grayImg
}

func worker(images <-chan string, wg *sync.WaitGroup) {
	defer wg.Done()
	for path := range images {
		start := time.Now()
		file, err := os.Open(path)
		if err != nil {
			log.Println("Error leyendo imagen:", err)
			continue
		}
		img, err := png.Decode(file)
		file.Close()
		if err != nil {
			log.Println("Error decodificando PNG:", err)
			continue
		}
		out := processImage(img)
		// Guardar resultado (opcional)
		outName := "processed_" + path
		outfile, err := os.Create(outName)
		if err == nil {
			jpeg.Encode(outfile, out, nil)
			outfile.Close()
		}
		log.Printf("Procesado %s en %v\n", path, time.Since(start))
	}
}

func main() {
	// Supongamos que tenemos 5 imágenes: img1.png, img2.png ...
	images := []string{"img1.png", "img2.png", "img3.png", "img4.png", "img5.png"}
	ch := make(chan string, len(images))
	var wg sync.WaitGroup

	// Crear N workers
	const numWorkers = 2
	for i := 0; i < numWorkers; i++ {
		wg.Add(1)
		go worker(ch, &wg)
	}

	// Enviar las imágenes a la cola
	for _, imgPath := range images {
		ch <- imgPath
	}
	close(ch)

	wg.Wait()
	fmt.Println("Fin de procesamiento concurrente")
}
