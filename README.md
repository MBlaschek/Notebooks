# Jupyter Notebooks

## Example Notebooks:
* Fernerkundung_python
* Solar_radiation
* statistics

## Scripts
mostly for linux or osx
### nb_server
Launch jupyter notebook server
```bash
nb_server -h -l -s -p []  --list --lab

Options:
  -h     Help
  -l     Launch Server(s)
  -s     Stop Server(s)
  -p []  Port
  --list List Notebook servers
  --lab  Launch lab instead of notebook

Show running Notebook Servers
jupyter notebook list

or
nb_server --list

Change Notebook Password:
jupyter notebook password

Last Change: Mit Okt  3 10:10:40 CEST 2018
Author: MB
```
Example Output:
`nb_server --list`
```bash
Running Notebook Servers HOSTNAME:
Access notebook (kill 6277) with: https://localhost:8888/ipython/
```


### jupyter_kernels.py
List jupyter kernels and connected Notebook file, and open files
```bash
jupyter_kernels.py [-f]
```
Example Output: `./jupyter_kernels.py -f`
```bash
##########
Servers:
URL: http://localhost:8888/ DIR: /home/user PID: 6277
##########
Kernels + Notebooks:
                                  ID     PID         PY Notebook
6345c823-33e2-4f36-ab45-2727a05c9ad5    6364    python3 /home/user/workspace/run/Tests.ipynb
2cfc3099-eab7-4b63-978d-6fb05d4e4269    6368    python3 /home/user/workspace/run/Detection_tests.ipynb
d0938098-c2b1-4f34-b281-beb3a9fcfa71    6375    python3 /home/user/workspace/run/Adjustment-Tests.ipynb
5cb462b0-7b4b-4f6d-8b94-7fca3c240709    6432    python3 /home/user/workspace/run/rasoTOOLS.ipynb
ca23b70e-265e-4d4e-9756-9f1bd6d346fa   15983    python3 /home/user/workspace/run/Detection_Norman.ipynb
Open files: 
ZMQbg/1 15983 user   44rR     REG                8,7  29799394 3145740 /home/user/workspace/raso_archive/072357/exp001.nc
ZMQbg/1 15983 user   55rR     REG                8,7 137383879 1838673 /home/user/workspace/raso_archive/072357/MARS_ODB.nc
---
31539fef-148c-40c6-9afa-ae4de1437dc2   28600    python3 /home/user/workspace/run/Detection.ipynb
Open files: 
ZMQbg/1 28600 user   45rR     REG                8,7  29771630 1708837 /home/user/workspace/raso_archive/011035/ERA.nc
ZMQbg/1 28600 user   46rR     REG                8,7  25778444 1709395 /home/user/workspace/raso_archive/011035/JRA55.nc
ZMQbg/1 28600 user   47rR     REG                8,7 344341767 1708831 /home/user/workspace/raso_archive/011035/MARS_ODB.nc
ZMQbg/1 28600 user   48rR     REG                8,7  12367179 1708836 /home/user/workspace/raso_archive/011035/CERA20C.nc
---
45deaf16-ff6a-4e97-bb98-9e579abb86af   14156    python3 /home/user/Documents/Lehre/Ensemble/WS2018/Blatt_08.ipynb
c305096d-c707-448c-92a0-2a6d78840801   19561    python2 /home/user/Documents/Lehre/Ensemble/WS2017/Blatt_09.ipynb
ae2096e5-c190-4adf-8148-47430a36eb42   19587    python2 /home/user/Documents/Lehre/Ensemble/WS2017/Blatt_08.ipynb
761d4e4a-ca7d-4547-9cf8-9f7ccbd7eab9    5256    python2 /home/user/Documents/Lehre/Ensemble/WS2018/Benotung_Ensemble.ipynb
b7a85d4a-2be0-4007-9427-f73fb27277c8    5906    python3 /home/user/Documents/Lehre/Ensemble/WS2018/Blatt_06.ipynb
6290bd6a-d9f3-4e8c-8f4c-57bc190e18d1    5926    python3 /home/user/Documents/Lehre/Ensemble/WS2018/Blatt_07.ipynb
ad11a214-7839-4f91-9f70-4e30686bb6ba    5949    python3 /home/user/Documents/Lehre/Ensemble/WS2018/Blatt_05.ipynb
f7a1d741-1aaf-4992-85b1-2e66de20f41d   15336    python2 /home/user/Documents/Lehre/Ensemble/WS2018/Ensemble Test.ipynb
458a2ef8-8254-4832-b5c6-b8a92d3bde58   15382    python3 /home/user/Documents/Lehre/Ensemble/WS2018/Blatt_02.ipynb
##########

```
