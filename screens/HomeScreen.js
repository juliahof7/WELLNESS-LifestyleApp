import React, { useState } from "react";
import { View, Text, TouchableOpacity, StyleSheet, Modal } from "react-native";

export function HomeScreen() {
  const [modalVisible, setModalVisible] = useState(false);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Find & Book Fitness Classes</Text>

      <TouchableOpacity style={styles.button} onPress={() => setModalVisible(true)}>
        <Text style={styles.buttonText}>Book Yoga Class</Text>
      </TouchableOpacity>

      {/* Modal for Booking */}
      <Modal animationType="slide" transparent={true} visible={modalVisible}>
        <View style={styles.modalView}>
          <Text style={styles.modalText}>Yoga Class Booked Successfully! 🎉</Text>
          <TouchableOpacity style={styles.closeButton} onPress={() => setModalVisible(false)}>
            <Text style={styles.buttonText}>Close</Text>
          </TouchableOpacity>
        </View>
      </Modal>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 20, justifyContent: "center", alignItems: "center" },
  title: { fontSize: 24, fontWeight: "bold", marginBottom: 20 },
  button: { backgroundColor: "#008080", padding: 15, borderRadius: 10 },
  buttonText: { color: "#fff", fontWeight: "bold" },
  modalView: { backgroundColor: "white", padding: 20, alignItems: "center", margin: 50, borderRadius: 10 },
  modalText: { fontSize: 18, marginBottom: 20 },
  closeButton: { backgroundColor: "#ff5a5f", padding: 10, borderRadius: 10 },
});
