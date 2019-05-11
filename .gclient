solutions = [
  {
    "name"        : "src/godot",
    "url"         : "https://github.com/godotengine/godot.git",
    "deps_file"   : "DEPS",
    "managed"     : True,
    "custom_deps" : {},
  },  
  {
    "name"        : "src/godot/modules/tensorflow",
    "url"         : "git@github.com:godot-extended-libraries/godot-tensorflow.git",
    "deps_file"   : "DEPS",
    "managed"     : True,
    "custom_deps" : {},
  },
  {
    "name"        : "src/godot/thirdparty/tensorflow",
    "url"         : "git@github.com:godot-extended-libraries/tensorflow.git",
    "deps_file"   : "DEPS",
    "managed"     : True,
    "custom_deps" : {},
  },
  {
    "name"        : "godot-tensorflow-demo",
    "url"         : "git@github.com:godot-extended-libraries/godot-tensorflow-demo.git",
    "deps_file"   : "DEPS",
    "managed"     : True,
    "custom_deps" : {},
  }
]
cache_dir = None