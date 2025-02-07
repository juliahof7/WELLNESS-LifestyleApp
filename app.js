import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { HomeScreen, MapsScreen, RecordScreen, GroupsScreen, ProfileScreen } from "./screens";
import { View, Text } from "react-native";
import { FontAwesome } from "@expo/vector-icons";

// Define bottom tab navigator
const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Tab.Navigator screenOptions={{ headerShown: false }}>
        <Tab.Screen name="Home" component={HomeScreen} options={{ tabBarIcon: ({ color }) => <FontAwesome name="home" size={24} color={color} /> }} />
        <Tab.Screen name="Maps" component={MapsScreen} options={{ tabBarIcon: ({ color }) => <FontAwesome name="map" size={24} color={color} /> }} />
        <Tab.Screen name="Record" component={RecordScreen} options={{ tabBarIcon: ({ color }) => <FontAwesome name="pencil" size={24} color={color} /> }} />
        <Tab.Screen name="Groups" component={GroupsScreen} options={{ tabBarIcon: ({ color }) => <FontAwesome name="users" size={24} color={color} /> }} />
        <Tab.Screen name="You" component={ProfileScreen} options={{ tabBarIcon: ({ color }) => <FontAwesome name="user" size={24} color={color} /> }} />
      </Tab.Navigator>
    </NavigationContainer>
  );
}
