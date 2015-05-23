# joycast
Capture and broadcast the best moments in your life<sup>*</sup>.

<sup>* best being defined as an Emotiv EPOC EEG headset saying that you smiled.</sup>

Mechanically, JoyCast is a Python script that monitors the lower jaw action and power output by the Emotiv Engine. When our classifier decides that you're over a happiness threshold, it takes a snapshot from your webcam and uploads it to Twitter.

For more information, see [Marie's post](http://www.mariehuynh.com/joycast-intelligent-automation-for-photos/).

Getting started
---------------

1. Install the Emotiv Xavier SDK and copy `edk.dll` (Windows), `libedk.so.1.0.0` (Linux), or `libedk.1.0.0.dylib` (Mac OS X) to the root of the repo.
2. Create a Twitter app at [https://apps.twitter.com/](https://apps.twitter.com/) and create `reference_code_snippets/keys.py` to expose your Twitter API keys. DO NOT COMMIT `keys.py`!
3. Install the tweepy Python module.
4. Install ImageMagick and make sure `convert` is in your path.
5. Windows: Download [CommandCam](https://batchloaf.wordpress.com/commandcam/) and put it in the root of the repository. Mac OS X: `sudo port install imagesnap`

Python files in the root of the repo should then be runnable. Our main executable is `launch_joycast.py`. You can dry-run it without posting to Twitter with the `-T` flag.

Gotchas
-------

* `Invalid Parameter - -rotate`: Windows has a `convert.exe` already. Hardcode the full path to convert in camera.py.

Contributors
------------
* Marie Huynh ([mariehuynh](https://github.com/mariehuynh))
* Nickolas Fotopoulos ([fotonick](https://github.com/fotonick))
* Derek Solven ([dsolven](https://github.com/dsolven))
* Joan Solven
