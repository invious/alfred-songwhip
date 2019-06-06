# alfred3-songkick
Automatically gives you links to the track on your clipboard for all music platforms provided by Songkick.

## Usage

Have a music link in your clipboard,

![](https://i.imgur.com/AHBHBro.png)

fire up Alfred and use the keyword. (default is 'sw'), and hit Enter

![](https://i.imgur.com/Ix1L6QK.png)

You will be presented with a choice of services to get a link for the song.

![](https://i.imgur.com/pGLhLPo.png)


## Issues
If you are having issues, check the debugger.

### Missing Python Packages

Best advice is to run `pip install --user -U pip` and then do `which python` to find your python executable.

You will also need to find the workflow data folder:

![](https://i.imgur.com/ESFMLvO.png)

```
pip install --user -U pip
/path/to/your/python -m pip i﻿nstall --target﻿ /workflow-data-folder requests
/path/to/your/python -m pip i﻿nstall --target﻿ /workflow-data-folder lxml
```
