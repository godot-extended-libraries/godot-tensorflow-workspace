## Tensorflow 2.0 for Godot 

ABANDONED because the lack of GPU tensorflow for the desktop.

<Wikipedia\> TensorFlow is a free and open-source software library for dataflow and differentiable programming across a range of tasks. It is a symbolic math library, and is also used for machine learning applications such as neural networks. 

This is Tensorflow for Godot Engine. The demo classifies an image into labels. This is a base for more interesting ideas like image upscaling, ai bots, chat bots, animations and others.

![Screen](https://github.com/godot-extended-libraries/godot-tensorflow-workspace/blob/master/Screen%20Shot%202019-05-13%20at%209.21.18%20PM.png)

## See also

https://github.com/godot-extended-libraries/godot-tensorflow

https://github.com/godot-extended-libraries/godot-tensorflow-demo

https://github.com/godot-extended-libraries/tensorflow

## Setup Instructions

* clone this repository `git clone https://github.com/godot-extended-libraries/godot-tensorflow-workspace.git --recursive`
* Go to the source `cd src/godot`.
* Compile godot using `scons platform=windows tools=yes -j8`. Your platform may be different.
* Open the example project `./bin/godot.windows.tools.64 --path ../../godot-tensorflow-demo/ -e` 
* Run the game `./bin/godot.windows.tools.64 --path ../../godot-tensorflow-demo/`
* See classification of the image

Use https://docs.godotengine.org/en/3.1/development/compiling/compiling_for_windows.html as reference.
