

<p align="center">
<a href="https://braindynamicslab.github.io/dyneusr/">
<img src="https://raw.githubusercontent.com/braindynamicslab/dyneusr/master/docs/assets/logo.png" height="250">
</a>
</p>


## **DyNeuSR Fire**

A command line interface for [DyNeuSR](https://braindynamicslab.github.io/dyneusr/) based on the [Python Fire](https://github.com/google/python-fire) library. 



## **Usage**

[DyNeuSR Fire](https://braindynamicslab.github.io/dyneusr-fire/) provides a command line interface for [DyNeuSR](https://braindynamicslab.github.io/dyneusr/). It wraps `kmapper` and `dyneusr` into a single pipeline, and uses the [Python Fire](https://github.com/google/python-fire) library to automatically generate a simple command line interface that accepts several important options and allows users to customize this pipeline. For more information about DyNeuSR, check out the [docs](https://braindynamicslab.github.io/dyneusr/).

To get started, check out the [examples](https://github.com/braindynamicslab/dyneusr-fire/tree/master/examples/), or try running one of the commands below on your own data.


### **_Basic Usage_** 

You can run the entire pipeline from the command line:
```bash
$ dyneusr-fire load_example --size=500 - run_mapper --projection=PCA(2) --resolution=10 --gain=0.5 - visualize
```


### **_Interactive Mode_** 

To run in interactive mode, you can run the following from the command line:
```bash
$ dyneusr-fire init -- --interactive
```

This will open an IPython shell.
```python
Fire is starting a Python REPL with the following objects:
Modules: fire, np, pd
Objects: Bunch, Cover, DBSCAN, DyNeuGraph, DyNeuSR, HDBSCAN, KMeans, KeplerMapper, MinMaxScaler, PCA, StandardScaler, TSNE, UMAP, check_estimator, component, f, result, self, trace

Python 3.7.2 | packaged by conda-forge | (default, Mar 19 2019, 20:46:22) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.3.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:                                                               
```

Then, you can step through the pipeline:
```python
In [1]: pipeline = DyNeuSR()

In [2]: pipeline.load_data(X='trefoil.npy', y='trefoil-target.npy')

In [3]: pipeline.run_mapper(projection=PCA(2), resolution=10, gain=0.5, clusterer=DBSCAN())

In [4]: pipeline.visualize()

```

Or, run it all at once:
```python
In [1]: DyNeuSR().load_example().run_mapper(projection=PCA(2), resolution=10, gain=0.5, clusterer=DBSCAN()).visualize()
```

Note, in the examples above, `load_example` is used for demo purposes only. You can replace `load_example` with `load_data` and load your own data by passing the file names of your data and target labels to the `X` and `y` arguments, respectively.




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

_To install from source:_
```bash
git clone https://github.com/braindynamicslab/dyneusr-fire.git
cd dyneusr-fire

pip install -e .
```


## **Support**

Please feel free to [report](https://github.com/braindynamicslab/dyneusr-fire/issues/new) any issues, [request](https://github.com/braindynamicslab/dyneusr-fire/issues/new) new features, or [propose](https://github.com/braindynamicslab/dyneusr-fire/compare) improvements. You can also contact Caleb Geniesse at geniesse [at] stanford [dot] edu.



## **Citation**

> Geniesse, C., Sporns, O., Petri, G., & Saggar, M. (2019). [Generating dynamical neuroimaging spatiotemporal representations (DyNeuSR) using topological data analysis](https://www.mitpressjournals.org/doi/abs/10.1162/netn_a_00093). *Network Neuroscience*. Advance publication. doi:10.1162/netn_a_00093
