# Wave function collapse maps

![image](./assets/example-map-v1.gif)

## Assets and inspiration

- This project is inspired by CodingQuest's video [here](https://youtu.be/qRtrj6Pua2A?si=8fVuqthD1DcrcTnX)
- Using 16x16 Mini World Sprites by Shade, which can be found [here](https://merchant-shade.itch.io/16x16-mini-world-sprites)
- You can read more about WFC [here](https://github.com/mxgmn/WaveFunctionCollapse). 


The core concept is that each tile in the window has an entropy (i.e. the possible sprites that can go there). Using context and the rules created we can reduce the entropy of a tile until it reduces to 0, meaning that a sprite has been assigned. Think of it as the logic that we use for solving Sudoku as explanined by [Martin Donald](https://youtu.be/2SuvO4Gi7uY?si=uMHMtL3reFOm6Msu). We apply a similar methodology.

The current version is rather simplistic, and somewhat bizarre seeming landmasses. I plan on continuing to iterate and improve upon that. 
Rules as they are currently set describe not just the neighbours a sprite can have, but also the weight assigned to each neighbour. 

## Installing

```shell
git clone https://github.com/sankomil/wave-function-collapse-map
cd wave-function-collapse-map
virtualenv venv
./venv/Scripts/activate
pip install -r requirements.txt
python main.py
```

## Plan of action
- [X] Create a basic somewhat working function of WFC 
- [] Fix logic and rules to create more logical seeming maps
- [] Add argument parsing when `main.py` is called from command line