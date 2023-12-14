from qiskit import *
%matplotlib inline
from qiskit.tools.visualization import plot_histogram

# Change this to change output integer size
num_qubits = 3

circuit = QuantumCircuit(num_qubits, num_qubits)

circuit.h(range(num_qubits))

circuit.barrier()

for i in range( num_qubits):
    circuit.measure(i, i)

circuit.barrier()

circuit.draw(output = 'mpl')

simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator, shots = 100000).result()
counts = result.get_counts()
plot_histogram(counts)