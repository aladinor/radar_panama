radar = pyart.io.read('./data/GUA191030231003.RAWCH8U')
display = pyart.graph.RadarMapDisplay(radar)
display.plot_ppi_map('reflectivity', sweep=0, vmin=-10, vmax=60,
                     resolution='10m')
