# Multiplicative Persistence

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

For context, read the [article on Medium](https://medium.com/@kevinrmcelwee/multiplicative-persistence-is-solved-1937692b26cc).

### Installation

With Python 3.7, run the following command:

```sh
pip install -r requirements.txt
```

### Execute search

The command...

```sh
python MPExplorer.py --start 475 --end 476
```

...will expand the two MP cubes from the powers 475 to 476.


### All Solutions
[`all_solutions.txt`](https://github.com/kmcelwee/multiplicative-persistence/blob/main/all_solutions.txt) contains the dictionary output from our algorithm. The first column, in the form "x,x,x,x,x,x,x,x" tells us the number of twos, threes, fours, fives, and so on in a number. (We don’t track the number of ones because there could be any number.) The second column contains the number itself, and the third column are the factors in the form (x, x, x, x). This gives us the number in terms of its factors (2<sup>x</sup>, 3<sup>x</sup>, 5<sup>x</sup>, 7<sup>x</sup>). 

For example, the number `117649` has one 4, one 7, one 6, and one 9 — so it is represented by `0,0,1,0,1,1,0,1`. It's equal to 7<sup>6</sup> so it's represented by `(0, 0, 0, 6)`.

### The JSON
[`dict_f475.json`](https://github.com/kmcelwee/multiplicative-persistence/blob/main/multiplicative_persistence/dict_f475.json) contains all the information in the `all_solutions.txt` file above. The dictionary is formatted such that when constructing the MP tree, we search for the next highest node. 

Say, for example, we are looking for a node upstream of 5. 5’s factors are 1 and 5, so we’d search for the key `‘0,0,0,1,0,0,0,0’`, and we are returned the list `[[5, (0, 0, 1, 0)], [15, (0, 1, 1, 0)]]`. We’ve found the upstream node 15, which can be factored into (3<sup>1</sup>)(5<sup>1</sup>). We are now looking for an upstream node that contains one three and one five. By plugging `‘0,1,0,1,0,0,0,0’` into the dictionary, we get back `[[35, (0, 0, 1, 1)], [315, (0, 2, 1, 1)], [135, (0, 3, 1, 0)]]`. We would continue this process until we reach a dead end.

### Visualizing MP Trees
The [`visualize_tree`](https://github.com/kmcelwee/multiplicative-persistence/blob/main/multiplicative_persistence/visualize_tree) folder contains functions that transform our main dictionary into a nested json that can be used in a D3 tree object, as shown in the Medium article.
