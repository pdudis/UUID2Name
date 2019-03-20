# UUID2Name
Substitutes the UUID filenames of [IUCLID](https://iuclid6.echa.europa.eu/project-iuclid-6) .i6z files with their entity names.

## Description
[IUCLID 6](https://iuclid6.echa.europa.eu/project-iuclid-6), by default, exports data using the filename convention "<UUID>.i6z" (i.e. "1cb2b9b5-b9bd-44ee-abe8-840856bbf5c6.i6z"). However, the need to distinguish such files by their Entity name arises quite often. Until now the usual method to find out the actual Entity name was to import the file into a [IUCLID 6](https://iuclid6.echa.europa.eu/project-iuclid-6) instance and open the concerned Entity. This process is time-consuming and tedious, especially when dealing with hundreds or even thousands of files. And, requires the presence of a [IUCLID 6](https://iuclid6.echa.europa.eu/project-iuclid-6) installation.

The UUID2Name tool, once pointed to a folder with UUID-named .i6z files, will automatically rename all such UUID filenames into their corresponding Entity names. Additionally, it will create a report in .csv format that outlines and maps the UUID filenames to the Entity names that substituted them.

## Usage 
`UUID2Name.py <path to folder that contains UUID .i6z filenames>`

## Requirements
- Python 3.x.x

## Notes
- Make sure to keep a backup of the folder fed to this tool, as the original files will be overwritten with the new filenames (you have been warned...)
- Files with identical Entity names are distinguished by adding incremented numbers at the end of their filenames
