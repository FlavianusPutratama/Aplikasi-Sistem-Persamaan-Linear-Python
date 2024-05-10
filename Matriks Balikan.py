import numpy as np

def solve_linear_system(A, b):
    """
    Fungsi ini menyelesaikan sistem persamaan linear Ax = b dengan menggunakan
    metode matriks balikan.
    
    Parameters:
        A (numpy.ndarray): Matriks koefisien dari sistem persamaan linear.
        b (numpy.ndarray): Vektor hasil dari sistem persamaan linear.
        
    Returns:
        x (numpy.ndarray): Solusi dari sistem persamaan linear.
    """
    A_inv = np.linalg.inv(A)  # Menghitung matriks balikan dari A
    x = np.dot(A_inv, b)      # Menghitung solusi x = A_inv * b
    return x

def main():
    # Input matriks koefisien A dan vektor hasil b
    A = np.array([[2, 1], [1, -3]])
    b = np.array([5, -3])
    
    # Memanggil fungsi untuk menyelesaikan sistem persamaan linear
    x = solve_linear_system(A, b)
    
    # Menampilkan solusi
    print("Solusi dari sistem persamaan linear adalah:")
    print(x)

if __name__ == "__main__":
    main()
