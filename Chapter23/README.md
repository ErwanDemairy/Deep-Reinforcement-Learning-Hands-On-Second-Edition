# Connect 4

## Train a network
`train.py --mps -n player1`
Produces states of neural network in the `./saves/player/' directory in the form `best_{%3d nb_round}_{%5d 00400.dat`

Note: `--mps` stands for metal, since cuda is not available on mac.

## Compare difference models

`play.py [--cuda] [--mps] [-r nb_rounds] model1 model2 ... modeln`
Make play each pair modeli, modelj, i != j for nb_rounds rounds (4 by default).
Gives a summary of the performances of each model.

## semi-final.sh
Make play all the models 00*, 01* ... (09* and 1*) together. There is a notebook file `final_plot.ipynb` in the tournament directory.