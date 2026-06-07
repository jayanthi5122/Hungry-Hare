import Navbar from "../components/Navbar.jsx";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";

function Location() {
  const restaurantPosition = [53.3498, -6.2603]; // Dublin

  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />

      <section className="max-w-5xl mx-auto px-6 py-12">
        <h1 className="text-5xl font-bold text-orange-600 mb-4">
          Our Restaurant Location 📍
        </h1>

        <p className="text-gray-600 mb-8">
          Hungry Hare Restaurant, Dublin, Ireland
        </p>

        <div className="h-[500px] rounded-3xl overflow-hidden shadow-xl">
          <MapContainer
            center={restaurantPosition}
            zoom={14}
            className="h-full w-full"
          >
            <TileLayer
              attribution="&copy; OpenStreetMap contributors"
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />

            <Marker position={restaurantPosition}>
              <Popup>
                Hungry Hare 🍔 <br />
                Dublin, Ireland
              </Popup>
            </Marker>
          </MapContainer>
        </div>
      </section>
    </div>
  );
}

export default Location;