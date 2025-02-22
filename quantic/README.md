
- Instalar Python
- Seleccionar carpeta quantic
  `cd quantic`
- Crear un entorno virtual
  `python -m venv quantic_env`
- Selecionar el entorno virtual
  `source quantic_env/bin/activate`
- Instalar dependencias
  ```bash
  pip install qiskit
  pip install qiskit-aer
  pip install qiskit-ibmq-provider
  pip install matplotlib
  # Instalar para ejemplos finales
  pip install pennylane
  pip install cirq
  ```
- Ejecutar ejemplos actualizados:
  ```bash
  python example1/fundamentos_qiskit_updated.py
  python example2/hadamard_circuit_updated.py
  ```
