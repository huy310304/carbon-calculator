# Carbon Footprint Calculator

## [A Short Demo on Youtube](https://youtu.be/Jo0kLyXL3QY)
This is a simple web application that calculates the carbon footprint based on user input for electricity usage, miles driven by car, meat consumption, and flight hours per year.  

## How To Use
1. **Clone the repository**: Use `git clone https://github.com/huy310304/carbon-calculator.git` to clone the repository to your local machine.
2. **Navigate to the project directory**: Open your terminal and change the directory to the `carbon-calculator` folder.
3. **Run the application**: Execute the command `python app.py` in your terminal to start the Flask web server. Make sure you have Flask installed (`pip install flask`) if needed.
4. **View the application**: Once the server is running, open your web browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to view and interact with the Carbon Footprint Calculator locally.

## Emission Factor References

### United States:
- **Electricity:** 0.41 kg CO2/kWh ([U.S. Environmental Protection Agency](https://www.epa.gov/ghgemissions/overview-greenhouse-gases#co2))
- **Transportation:** 0.24 kg CO2/mile ([U.S. Department of Energy](https://afdc.energy.gov/data/10309))
- **Meat:** 25 kg CO2/kg (average estimate)
- **Flights:** 0.11 kg CO2/passenger mile ([U.S. Department of Energy](https://afdc.energy.gov/data/10309))

### European Union:
- **Electricity:** 0.3 kg CO2/kWh ([European Environment Agency](https://www.eea.europa.eu/))
- **Transportation:** 0.12 kg CO2/km ([European Environment Agency](https://www.eea.europa.eu/))
- **Meat:** 25 kg CO2/kg (average estimate)
- **Flights:** 0.22 kg CO2/passenger km ([European Environment Agency](https://www.eea.europa.eu/))

### Asia:
- **Electricity:** 0.75 kg CO2/kWh (average estimate for major Asian countries)
- **Transportation:** 0.2 kg CO2/km (varies widely by country and transportation mode)
- **Meat:** 25 kg CO2/kg (average estimate)
- **Flights:** 0.22 kg CO2/passenger km (varies by airline and route)

These values are approximate estimates based on available data and may not represent the exact emission factors for each region.
