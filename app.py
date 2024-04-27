from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Retrieve data from form
        electricity = float(request.form['electricity'])
        miles = float(request.form['miles'])
        meat = float(request.form['meat'])
        flights = float(request.form['flights'])
        region = request.form['region']  # Retrieve selected region
        
        # Define emission factors based on region
        if region == 'us':
            # Emission factors for the United States
            electricity_factor = 0.41  # kg CO2/kWh (U.S. EPA)
            transportation_factor = 0.24  # kg CO2/mile (U.S. DOE)
            meat_factor = 25  # kg CO2/kg (average estimate)
            flights_factor = 0.11  # kg CO2/passenger mile (U.S. DOE)
        elif region == 'eu':
            # Emission factors for the European Union
            electricity_factor = 0.3  # kg CO2/kWh (EU average)
            transportation_factor = 0.12  # kg CO2/km (EEA)
            meat_factor = 25  # kg CO2/kg (average estimate)
            flights_factor = 0.22  # kg CO2/passenger km (EEA)
        elif region == 'asia':
            # Emission factors for Asia
            electricity_factor = 0.75  # kg CO2/kWh (average estimate for China and India)
            transportation_factor = 0.2  # Assume a higher value to account for variability
            meat_factor = 25  # kg CO2/kg (average estimate)
            flights_factor = 0.22  # Assume a value similar to EU for simplicity
        else:
            # Handle unknown region
            return jsonify({"error": "Unknown region"})
        
        # Calculate carbon footprint using region-specific factors
        carbon_footprint = {
            "electricity": electricity * electricity_factor,
            "transportation": miles * transportation_factor,
            "meat": meat * meat_factor,
            "flights": flights * flights_factor
        }
        
        # Determine recommendations based on carbon footprint
        recommendations = []
        total_footprint = sum(carbon_footprint.values())
        
        # Energy efficiency recommendations
        if electricity > 0:
            energy_recommendation = "Consider using energy-efficient appliances and switching to renewable energy sources where possible to reduce electricity-related emissions."
            recommendations.append(energy_recommendation)
        
        # Transportation recommendations
        if miles > 0:
            transportation_recommendation = "Try to use public transportation, carpool, bike, or walk whenever possible to reduce transportation-related emissions."
            recommendations.append(transportation_recommendation)
        
        # Dietary recommendations
        if meat > 0:
            dietary_recommendation = "Reducing meat consumption, particularly red meat, can significantly lower your carbon footprint. Consider incorporating more plant-based meals into your diet."
            recommendations.append(dietary_recommendation)
        
        # Flight recommendations
        if flights > 0:
            flight_recommendation = "Minimize air travel and consider alternative modes of transportation for long distances. If you must fly, opt for direct flights and consider carbon offsetting options."
            recommendations.append(flight_recommendation)
        
                # Prepare data for chart
        labels = list(carbon_footprint.keys())
        data = list(carbon_footprint.values())
        
        return jsonify({"carbon_footprint": carbon_footprint, "chart_labels": labels, "chart_data": data, "recommendations": recommendations})
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
