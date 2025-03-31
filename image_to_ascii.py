from PIL import Image
def image_to_ascii(image, type, saveas="output.txt", quality=3):
    scale = int(quality)
    img = Image.open((image+"."+type))
    w,h = img.size
    img.resize((w//quality, h//quality))
    w, h = img.size
    grid = []
    for i in range(h):
        grid.append(["X"] * w)

    pix = img.load()


    for y in range(h):
        for x in range(w):
            if sum(pix[x,y]) == 0:
                grid[y][x] = "#"
            elif sum(pix[x,y]) in range(1,100):
                grid[y][x] = "X"
            elif sum(pix[x,y]) in range(100,150):
                grid[y][x] = "@"
            elif sum(pix[x,y]) in range(150,250):
                grid[y][x] = "%"
            elif sum(pix[x,y]) in range(250,350):
                grid[y][x] = "&"
            elif sum(pix[x,y]) in range(350,450):
                grid[y][x] = "*"
            elif sum(pix[x,y]) in range(450,550):
                grid[y][x] = "+"
            elif sum(pix[x,y]) in range(550,650):
                grid[y][x] = "/"
            elif sum(pix[x,y]) in range(650,750):
                grid[y][x] = "("
            elif sum(pix[x,y]) in range(750,800):
                grid[y][x] = "'"
            elif sum(pix[x,y]) in range(800,850):
                grid[y][x] = "."
            else:
                grid[y][x] = " "
                
    art = open(saveas, "w")

    for row in grid:
        art.write("".join(row)+"\n")

    art.close()

file_name = "image"#YOUR FILE HERE
type = "jpg"#YOUR FILE TYPE
saveas = "output.txt"#NAME OF YOUR OUTPUT FILE
quality = 3#RANGE QUALITY HERE, MAY SLOW YOUR MACHINE


if __name__ == '__main__':
    image_to_ascii(image=file_name, type=type, saveas="output.txt", quality=quality)

# This project is purely expirimental. Any type of use is prohibited and not
# in the responsibility of 'FireballCreep3r'.
# The text image is currently takes up x3 of original image if max quality.
# This project may be updated in the future.
# © Created by FireballCreep3r on Github. Main code forkey by 'Isak Solheim'.
