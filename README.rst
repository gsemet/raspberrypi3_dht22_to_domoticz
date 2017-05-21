Installation:
=============

- clone this project to your Raspberry Pi
- execute `./build.sh`
- edit `config.yaml` according to your configuration
- add this line to your crontab (use `crontab -e`):

    */5 * * * * /path/to/run.sh
