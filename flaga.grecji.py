width = 27 * 10
height = 18 * 10

with open("grecja.2.ppm","w") as f:
    f.write("P3\n")
    f.write(f"{width} {height}\n")
    f.write("255\n")
    for y in range(height):
        for x in range(width):
            if x < width * (10/27) and y < height * (10/18):
                if (4/27) * width <= x < (6/27) * width or (4/18) * height <= y < (6/18) * height:
                    f.write(f"{255} {255} {255}\n")
                else:
                    f.write(f"{13} {94} {175}\n")
            else:
                for n in range(9):
                    if n % 2 == 0 and y >= (n/9) * height and y < ((n+1)/9) * height:
                        f.write(f"{13} {94} {175}\n")
                    if n % 2 == 1 and y >= (n/9) * height and y < ((n+1)/9) * height:
                        f.write(f"{255} {255} {255}\n") 