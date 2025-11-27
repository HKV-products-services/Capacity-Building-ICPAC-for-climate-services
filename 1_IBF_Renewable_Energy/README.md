# Renewable Energy Forecasting

This folder contains code, notebooks and data references used to prepare and evaluate renewable energy forecasts (solar, wind, hydropower) using ERA5 reanalysis, AIFS forecasts and local climatologies. 

## Install environment

Open the terminal and run:

```bash
pixi install
```

After installing run the following to add the kernel to Jupyter:

```bash
pixi run setup-kernel
```

Finally you are able to start Jupyter Lab with:

```bash
pixi run notebook
```

## What you'll find here

- Notebooks that walk through data preprocessing and power calculations (see `*.ipynb`).
- Example scripts for plotting and quick checks (`plot.py`).
- A `data/` directory (not all raw data is stored in the repository — see Data section).


## Download data
* **Download the data from this clicking wetransfer link**: https://we.tl/t-iymNkGIpC2
* There is a password that will be provided during the workshop. 

## Quick start

1. Install Pixi (this project uses Pixi to manage dependencies and environments): https://pixi.sh/latest/installation/
2. From the `Renewable_Energy_Forecasting` folder run:

```bash
pixi install
```

3. Open the notebooks (for example `1_Preprocess_ERA5_data.ipynb`) in Jupyter / VS Code and follow the step-by-step analysis.

## Data layout and required files

Place required input files in the `data/` directory using the following structure (relative to this folder):

- `data/AIFS/output/` — AIFS forecast files, named like `YYYYMMDDHHMMSS-step-var.nc` (e.g. `20251031000000-360h_tp.nc`). These are the forecast inputs used by the notebooks.
- `data/climatology/` — climatology files such as `surface_solar_radiation_downwards_climatology.nc`.
- `data/ERA5/` — ERA5-derived inputs (example: `surface_solar_radiation_downwards_stream-oper_daily-mean.nc`).


Download from this wetranfer link:
    * 

## Notebooks and scripts

- `1_Preprocess_ERA5_data.ipynb` — prepare ERA5 data used in radiation / power calculations.
- `2_Get_AIFS_forecast.ipynb` — download/prepare AIFS forecast fields for the study domain and horizon.
- `3_Solar_Power_Generation.ipynb` — example solar PV generation calculation from radiation inputs.
- `4_Wind_Power_Output.ipynb` — wind power output estimation from wind fields.
- `5_Hydropower.ipynb` — hydropower-related preprocessing and examples.
- `plot.py` — small helper for plotting results used by notebooks.

Open these notebooks interactively. They include runnable cells and short explanations.
