import math


def euclidean_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)


def main():
    points = []
    
    
    n = int(input("Kaç nokta gireceksiniz? "))
    
    for i in range(n):
        x = float(input(f"{i + 1}. noktanın x koordinatını girin: "))
        y = float(input(f"{i + 1}. noktanın y koordinatını girin: "))
        points.append((x, y))
    
    # Mesafeleri saklamak için liste
    distances = []
    
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclidean_distance(points[i], points[j])
            distances.append(distance)
            print(f"Mesafe {points[i]} ve {points[j]} arasındaki: {distance:.2f}")
    
   
    min_distance = min(distances)
    print(f"Minimum mesafe: {min_distance:.2f}")

if __name__ == "__main__":
    main()