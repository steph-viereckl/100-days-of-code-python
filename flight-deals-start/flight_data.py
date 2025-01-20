class FlightData:

    def __init__(self, price, dept_iata_code, arrive_iata_code, outbound_date, inbound_date):
        self.price = price
        self.departure_iata_code = dept_iata_code
        self.arrival_iata_code = arrive_iata_code
        self.outbound_date = outbound_date
        self.inbound_date = inbound_date