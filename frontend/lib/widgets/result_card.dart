import 'package:flutter/material.dart';

import '../models/prediction_response.dart';

class ResultCard extends StatelessWidget {
  final PredictionResponse result;

  const ResultCard({
    super.key,
    required this.result,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 4,
      margin: const EdgeInsets.symmetric(vertical: 12),
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              'Prediction Result',
              style: TextStyle(
                fontSize: 22,
                fontWeight: FontWeight.bold,
              ),
            ),

            const SizedBox(height: 20),

            _buildRow(
              'Success Probability',
              '${result.successProbability.toStringAsFixed(2)}%',
            ),

            _buildRow(
              'Business Score',
              result.businessScore.toStringAsFixed(2),
            ),

            _buildRow(
              'AI Score',
              result.overallAiScore.toStringAsFixed(2),
            ),

            _buildRow(
              'Status',
              result.overallStatus,
            ),

            _buildRow(
              'Grade',
              result.grade,
            ),

            _buildRow(
              'Decision',
              result.decision,
            ),

            _buildRow(
              'Confidence',
              result.confidence,
            ),

            _buildRow(
              'Risk Level',
              result.riskLevel,
            ),

            _buildRow(
              'Recommendation',
              result.recommendation,
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildRow(
    String title,
    String value,
  ) {
    return Padding(
      padding: const EdgeInsets.symmetric(
        vertical: 7,
      ),
      child: Row(
        mainAxisAlignment:
            MainAxisAlignment.spaceBetween,
        children: [
          Text(
            title,
            style: const TextStyle(
              fontWeight: FontWeight.w600,
            ),
          ),
          Flexible(
            child: Text(
              value,
              textAlign: TextAlign.right,
            ),
          ),
        ],
      ),
    );
  }
}