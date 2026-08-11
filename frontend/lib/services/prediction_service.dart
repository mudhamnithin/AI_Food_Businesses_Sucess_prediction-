import 'dart:convert';

import 'package:http/http.dart' as http;

import '../models/prediction_request.dart';
import '../models/prediction_response.dart';

class PredictionService {
  static const String baseUrl =
      'https://ai-food-businesses-sucess-prediction-2.onrender.com/api/predict/';

  Future<PredictionResponse> predict(
    PredictionRequest request,
  ) async {
    final response = await http.post(
      Uri.parse(baseUrl),
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
      body: jsonEncode(request.toJson()),
    );

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);

      return PredictionResponse.fromJson(data);
    }

    throw Exception(
      'Prediction failed: ${response.statusCode}',
    );
  }
}