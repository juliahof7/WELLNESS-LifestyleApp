import React from "react";
import { View, Text, Image, TouchableOpacity, StyleSheet, ScrollView, TextInput } from "react-native";

export default function HomeScreen() {
  return (
    <ScrollView style={styles.container}>
      {/* Header Section */}
      <View style={styles.header}>
        <Image source={require("../../assets/profile-icon.png")} style={styles.profileIcon} />
        <View>
          <Text style={styles.appTitle}>WELLNESS - Lifestyle App</Text>
          <Text style={styles.userInfo}>Current Location: San Diego</Text>
          <Text style={styles.userInfo}>Dietary Restrictions: Vegetarian</Text>
        </View>
      </View>

      {/* Saved Favorites */}
      <Text style={styles.sectionTitle}>Saved Favorites</Text>
      <View style={styles.favorites}>
        <TouchableOpacity style={styles.favoriteItem}>
          <Image source={require("../../assets/restaurant-icon.png")} style={styles.icon} />
          <Text>Restaurants</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.favoriteItem}>
          <Image source={require("../../assets/fitness-icon.png")} style={styles.icon} />
          <Text>Fitness</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.favoriteItem}>
          <Image source={require("../../assets/eco-icon.png")} style={styles.icon} />
          <Text>Eco-Friendly</Text>
        </TouchableOpacity>
      </View>

      {/* Search Bar */}
      <TextInput placeholder="Search locations" style={styles.searchBar} />

      {/* Nearby Section */}
      <Text style={styles.sectionTitle}>Nearby</Text>
      <View style={styles.favorites}>
        <TouchableOpacity style={styles.favoriteItem}>
          <Image source={require("../../assets/restaurant-icon.png")} style={styles.icon} />
          <Text>Restaurants</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.favoriteItem}>
          <Image source={require("../../assets/fitness-icon.png")} style={styles.icon} />
          <Text>Fitness</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.favoriteItem}>
          <Image source={require("../../assets/eco-icon.png")} style={styles.icon} />
          <Text>Eco-Friendly</Text>
        </TouchableOpacity>
      </View>

      {/* Bottom Navigation */}
      <View style={styles.bottomNav}>
        <TouchableOpacity><Text> Home</Text></TouchableOpacity>
        <TouchableOpacity><Text>📍 Maps</Text></TouchableOpacity>
        <TouchableOpacity><Text>📖 Record</Text></TouchableOpacity>
        <TouchableOpacity><Text>👥 Groups</Text></TouchableOpacity>
        <TouchableOpacity><Text>👤 You</Text></TouchableOpacity>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: "#F5F5F5", padding: 20 },
  header: { flexDirection: "row", alignItems: "center", marginBottom: 20 },
  profileIcon: { width: 50, height: 50, marginRight: 10 },
  appTitle: { fontSize: 20, fontWeight: "bold" },
  userInfo: { fontSize: 14, color: "gray" },
  sectionTitle: { fontSize: 18, fontWeight: "bold", marginVertical: 10 },
  favorites: { flexDirection: "row", justifyContent: "space-between" },
  favoriteItem: { alignItems: "center", padding: 10 },
  icon: { width: 50, height: 50, marginBottom: 5 },
  searchBar: { backgroundColor: "white", padding: 10, borderRadius: 10, marginVertical: 10 },
  bottomNav: { flexDirection: "row", justifyContent: "space-around", marginTop: 20, padding: 10, backgroundColor: "white" },
});
