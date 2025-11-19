"""
Plotting utilities for climate and weather data visualization.
"""
from typing import Any, Dict, Optional, Tuple

import cartopy.crs as ccrs  # type: ignore
import matplotlib.pyplot as plt
import xarray as xr


def plot_variable(
    ds: xr.Dataset,
    var_name: str,
    forecast_datetime_str: Optional[str] = None,
    step: Optional[int] = 0,
    figsize: Tuple[float, float] = (12, 6),
    cmap: str = "viridis",
    projection: Optional[Any] = None,
    title: Optional[str] = None,
    cbar_label: Optional[str] = None,
    vmin: Optional[float] = None,
    vmax: Optional[float] = None,
    coastline_kwargs: Optional[Dict[str, Any]] = None,
    add_gridlines: bool = True,
    show: bool = True,
    save_path: Optional[str] = None,
    dpi: int = 150,
    **plot_kwargs: Any,
) -> Tuple[Any, Any]:
    """
    Plot a variable from an xarray Dataset on a map.
    
    Args:
        ds: xarray Dataset containing the variable to plot
        var_name: Name of the variable to plot
        forecast_datetime_str: Forecast initialization time string for title (optional)
        step: Time step index to plot (default: 0). If None, plots all times or assumes no step dimension
        figsize: Figure size as (width, height) in inches
        cmap: Colormap name (default: 'viridis')
        projection: Cartopy projection (default: PlateCarree())
        title: Custom title (overrides automatic title)
        cbar_label: Label for colorbar (default: uses variable attributes or name)
        vmin: Minimum value for colorbar (default: auto)
        vmax: Maximum value for colorbar (default: auto)
        coastline_kwargs: Additional kwargs for coastlines (e.g., {'linewidth': 0.5, 'color': 'black'})
        add_gridlines: Whether to add gridlines (default: True)
        show: Whether to display the plot (default: True)
        save_path: Path to save the figure (optional)
        dpi: DPI for saved figure (default: 150)
        **plot_kwargs: Additional kwargs passed to pcolormesh
        
    Returns:
        Tuple of (figure, axes)
    """
    if projection is None:
        projection = ccrs.PlateCarree()
    
    # Create figure and axes
    fig = plt.figure(figsize=figsize)
    ax = plt.axes(projection=projection)
    
    # Select data to plot
    data = ds[var_name]
    if step is not None and "step" in data.dims:
        data = data.isel(step=step)
    elif "time" in data.dims and step is not None:
        data = data.isel(time=step)
    
    # Prepare colorbar label
    if cbar_label is None:
        # Try to get units from variable attributes
        units = data.attrs.get("units", data.attrs.get("unit", ""))
        long_name = data.attrs.get("long_name", var_name)
        if units:
            cbar_label = f"{long_name} ({units})"
        else:
            cbar_label = long_name
    
    # Prepare plot kwargs
    pcolormesh_kwargs = {
        "ax": ax,
        "transform": ccrs.PlateCarree(),
        "cmap": cmap,
        "cbar_kwargs": {"label": cbar_label},
    }
    if vmin is not None:
        pcolormesh_kwargs["vmin"] = vmin
    if vmax is not None:
        pcolormesh_kwargs["vmax"] = vmax
    
    # Merge with user-provided kwargs
    pcolormesh_kwargs.update(plot_kwargs)
    
    # Plot the data
    data.plot.pcolormesh(**pcolormesh_kwargs)
    
    # Add coastlines
    coastline_defaults = {"linewidth": 0.8, "color": "black"}
    if coastline_kwargs:
        coastline_defaults.update(coastline_kwargs)
    ax.coastlines(**coastline_defaults)
    
    # Add gridlines
    if add_gridlines:
        gl = ax.gridlines(draw_labels=True, linewidth=0.5, alpha=0.5, linestyle="--")
        gl.top_labels = False
        gl.right_labels = False
    
    # Set title
    if title is None:
        if forecast_datetime_str and step is not None:
            title = f"ECMWF Forecast {var_name} (run: {forecast_datetime_str}, step: +{step}h)"
        elif forecast_datetime_str:
            title = f"ECMWF Forecast {var_name} (run: {forecast_datetime_str})"
        else:
            title = f"{var_name}"
    ax.set_title(title)
    
    # Save if requested
    if save_path:
        fig.savefig(save_path, dpi=dpi, bbox_inches="tight")
        print(f"Figure saved to {save_path}")
    
    # Show if requested
    if show:
        plt.show()
    
    return fig, ax
