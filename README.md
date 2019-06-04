

<p align="center">
<a href="https://braindynamicslab.github.io/dyneusr/">
<img src="https://raw.githubusercontent.com/braindynamicslab/dyneusr/master/docs/assets/logo.png" height="250">
</a>
</p>


## **DyNeuSR Fire**

A command line interface for [DyNeuSR](https://braindynamicslab.github.io/dyneusr/) based on the [Python Fire](https://github.com/google/python-fire) library. 



## **Usage**

[DyNeuSR Fire](https://braindynamicslab.github.io/dyneusr-fire) provides a command line interface that wraps [`kmapper`](kepler-mapper.scikit-tda.org) graph generation and [`dyneusr`](https://braindynamicslab.github.io/dyneusr) visualization into a single executable. It uses the [`python-fire`](https://github.com/google/python-fire) library to automatically generate a simple command line interface that accepts several important options and allows users to customize this pipeline.

To get started, check out the [examples](https://github.com/braindynamicslab/dyneusr-fire/tree/master/examples/), or try running one of the commands below on your own data.


### **_Basic Usage_** 

```bash
dyneusr-fire load_data --X=trefoil.npy - run_mapper --resolution=10 --gain=0.2 - visualize
```


### **_Interactive Mode_** 

```bash
dyneusr-fire load_data init -- --interactive
```

```python
Fire is starting a Python REPL with the following objects:
Modules: fire, np, pd
Objects: Bunch, Cover, DBSCAN, DyNeuGraph, DyNeuSR, HDBSCAN, KMeans, KeplerMapper, MinMaxScaler, PCA, StandardScaler, TSNE, UMAP, check_estimator, component, f, result, self, trace

Python 3.7.2 | packaged by conda-forge | (default, Mar 19 2019, 20:46:22) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.3.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:                                                               
```

```python
In [1]: pipeline = DyNeuSR()
```

```python
In [2]: pipeline.load_example()
```

```python
In [3]: pipeline.run_mapper()
```

```python
In [4]: pipeline.visualize()

```

Or, all together:

```python
In [1]: DyNeuSR().load_example().run_mapper().visualize()
```

Note, in the examples above, `load_example` can be replaced with `load_data` to load your own data.




## **Setup**

### **_Dependencies_**

#### [Python 3.6+](https://www.python.org/)

#### Required Python Packages
* [fire](https://github.com/google/python-fire)
* [dyneusr](https://braindynamicslab.github.io/dyneusr)
* [kmapper](kepler-mapper.scikit-tda.org)
* [sklearn](https://scikit-learn.org/)
* [umap-learn](https://github.com/lmcinnes/umap)
* [hdbscan](https://github.com/scikit-learn-contrib/hdbscan)


### **_Install with PIP_**

_To install with pip:_
```bash
pip install dyneusr-fire
```


## **Support**

Please feel free to [report](https://github.com/braindynamicslab/dyneusr-fire/issues/new) any issues, [request](https://github.com/braindynamicslab/dyneusr-fire/issues/new) new features, or [propose](https://github.com/braindynamicslab/dyneusr-fire/compare) improvements. You can also contact Caleb Geniesse at geniesse [at] stanford [dot] edu.



## **Citation**

> Geniesse, C., Sporns, O., Petri, G., & Saggar, M. (2019). [Generating dynamical neuroimaging spatiotemporal representations (DyNeuSR) using topological data analysis](https://www.mitpressjournals.org/doi/abs/10.1162/netn_a_00093). *Network Neuroscience*. Advance publication. doi:10.1162/netn_a_00093
