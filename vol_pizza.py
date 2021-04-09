def vol_pizza(radius, height):
    return (22 * radius * radius * height) // 7

if __name__ == "__main__":
    radius, height = map(int, input().split())
    result = vol_pizza(radius, height)
    print(result)
