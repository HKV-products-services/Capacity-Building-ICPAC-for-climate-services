# Renewable Energy Forecasting

This folder contains code, notebooks and data references used to prepare and evaluate renewable energy forecasts (solar, wind, hydropower) using ERA5 reanalysis, AIFS forecasts and local climatologies. 

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


# Deployment guide (short)

This repository includes a sample production Dockerfile (`Dockerfile.prod`) and CI/CD templates (`cloudbuild.yaml`, `.github/workflows/deploy.yml`) to deploy to Google Cloud Run via Artifact Registry.

Quick steps:

1. Create GCP project and enable APIs (Artifact Registry, Cloud Run, Cloud Build).
2. Create two service accounts (deploy + runtime) as documented in the notebooks and grant required roles.
3. Store the deployer service account key in GitHub secret `GCP_SA_KEY` and project ID in `GCP_PROJECT_ID`.
4. Ensure `requirements.txt` exists and lists the application dependencies.
5. Push to `main` — GitHub Actions will build, push and deploy the image.

Files added:
- `Dockerfile.prod` - production Dockerfile for the app
- `cloudbuild.yaml` - example cloud build pipeline
- `.github/workflows/deploy.yml` - GitHub Actions workflow for deployment

Notes:
- Adjust worker counts and CPU/memory settings for Cloud Run according to your expected load.
- Treat service account keys as sensitive; rotate and limit permissions regularly.
