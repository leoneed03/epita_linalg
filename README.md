# epita_linalg
change of basis, linear algebra project

## Dependencies

```
python3 -m venv ./venv  
. venv/bin/activate          
pip install --upgrade pip    
pip install -r requirements.txt
```

## Usage

Just run 
```
python3 main.py
```

Program will ask you to input number of dimensions for the problem `N`, then vector of size `N`
example vector input for `N=2`:
```
-1.1,-3.2
```
If your vector is represented using non-canonical basis,
you will be asked to input matrix representing it (each column is a basis vector with respect to the canonical basis). 
Then you will be asked to input NEW basis in the same format

example basis matrix input for `N=2`:
```
-5.1,-10.2
20.5,30.4
```

If `N=2` then you will be asked if you want to save plotted basises and your vector.
Just accept and input a filename where to save the plot

