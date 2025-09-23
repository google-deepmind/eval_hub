We will count each possible configuration of colors placed on the top of the red cubes separately. First, we'll split the configurations by the number of white cubes, and then by the number of blue and green cubes.

***

## Configurations by White Cube Count

* **0 White Cubes**
    * 4 Blue (4B): 72 options
    * 4 Green (4G): 72 options
    * 1 Green, 3 Blue (1G 3B): 96 options
    * 1 Blue, 3 Green (1B 3G): 96 options
    * Alternating Blue/Green (BGBG): 32 options
    * 2 Blue, 2 Green (BBGG): 96 options

* **1 White Cube**
    * 3 Blue (3B): 96 options
    * 3 Green (3G): 96 options
    * Blue-Green-Blue (BGB): 32 options
    * Green-Blue-Green (GBG): 32 options
    * GGB + BGG: 88 options
    * BBG + GBB: 88 options

* **2 White Cubes**
    * Adjacent (WW--): 240 options
    * Alternating (W-W-): 48 options

* **3 White Cubes**
    * 1 Blue (B): 64 options
    * 1 Green (G): 64 options

* **4 White Cubes**: 48 options

***

## Total Count

After summing all the options, we get a total count of **1360**.
