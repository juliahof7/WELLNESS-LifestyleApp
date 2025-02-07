import React from "react";
import { View, StyleSheet } from "react-native";
import MapView, { Marker } from "react-native-maps";

export function MapsScreen() {
  const fitnessCenters = [
    { id: 1, title: "Yoga Studio", latitude: 37.78825, longitude: -122.4324 },
    { id: 2, title: "Pilates Center", latitude: 37.78925, longitude: -122.4344 },
    { id: 3, title: "LifeTime Fitness", latitude: 37.78725, longitude: -122.4364 },
  ];

  return (
    <View style={styles.container}>
      <MapView 
        style={styles.map}
        initialRegion={{
          latitude: 37.78825,
          longitude: -122.4324,
          latitudeDelta: 0.01,
          longitudeDelta: 0.01,
        }}
      >
        {fitnessCenters.map((place) => (
          <Marker key={place.id} coordinate={{ latitude: place.latitude, longitude: place.longitude }} title={place.title} />
        ))}
      </MapView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1 },
  map: { width: "100%", height: "100%" },
});
