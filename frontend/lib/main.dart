import 'package:flutter/material.dart';

import 'screens/home_screen.dart';

void main() {
  runApp(const FoodBusinessPredictionApp());
}

class FoodBusinessPredictionApp extends StatelessWidget {
  const FoodBusinessPredictionApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Food Business Prediction',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: Colors.green,
        ),
        useMaterial3: true,
      ),
      home: const HomeScreen(),
    );
  }
}