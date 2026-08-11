import 'package:flutter/material.dart';

class ModelPerformanceCard extends StatelessWidget {
  const ModelPerformanceCard({super.key});

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 4,
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Row(
              children: [
                Icon(Icons.analytics),
                SizedBox(width: 10),
                Text(
                  'AI Model Performance',
                  style: TextStyle(
                    fontSize: 22,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ],
            ),

            const SizedBox(height: 20),

            _metric(
              'Accuracy',
              '94%',
            ),

            _metric(
              'Precision',
              '84%',
            ),

            _metric(
              'Recall',
              '90%',
            ),

            _metric(
              'F1 Score',
              '87%',
            ),

            _metric(
              'Cross Validation',
              '92.56% ± 1.43%',
            ),
          ],
        ),
      ),
    );
  }

  Widget _metric(
    String name,
    String value,
  ) {
    return Padding(
      padding: const EdgeInsets.symmetric(
        vertical: 8,
      ),
      child: Row(
        mainAxisAlignment:
            MainAxisAlignment.spaceBetween,
        children: [
          Text(
            name,
            style: const TextStyle(
              fontWeight: FontWeight.w600,
            ),
          ),
          Text(
            value,
            style: const TextStyle(
              fontWeight: FontWeight.bold,
            ),
          ),
        ],
      ),
    );
  }
}