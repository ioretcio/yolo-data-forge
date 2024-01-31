
# yolo-data-forge

  

Yolo Data Forge is a specialized toolkit tailored for YOLO (You Only Look Once) object detection models, offering a robust set of tools for crafting, refining, and augmenting datasets. This tool suite facilitates the preparation of annotated data, enabling smoother training and enhanced accuracy for YOLO-based artificial intelligence applications.

  

##	Progress

							common:

- [x] empty pictures finder

- [x] train-val-test splitter

- [x] 4k to fullHD patcher (1to4)

- [x] part_mover

- [x] recursively latinizer

- [ ] huge images pather to fixSized patches

- [x] brightness sort

							hash db:

- [x] dataset fingerprint creator

- [x] dataset fingerprint database_x_folder intersection

- [x] dataset fingerprint database_x_database intersection

- [x] deleter all dublicates files from purgelist.txt

							converts:

- [x] convert obb-labelimg

- [ ] convert yolo-labelimg

- [ ] convert dota-labelimg

							decimators:

- [x] exact copies cleaner

- [x] structural similarity test (DECIMATOR)

							help:

- [x] description (updating)

### Installation and updating:
```
pip install --upgrade --force-reinstall git+https://github.com/ioretcio/yolo-data-forge
```
### About:
(after installation. Without python.. stuff)
```
df_about
```