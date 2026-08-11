import 'package:flutter/material.dart';

import '../models/prediction_response.dart';

class ResultScreen extends StatelessWidget {
  final PredictionResponse result;

  const ResultScreen({
    super.key,
    required this.result,
  });

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF7FAF2),
      appBar: AppBar(
        title: const Text('Prediction Result'),
        centerTitle: true,
        elevation: 0,
      ),
      body: SafeArea(
        child: LayoutBuilder(
          builder: (context, constraints) {
            return SingleChildScrollView(
              padding: const EdgeInsets.all(16),
              child: Center(
                child: SizedBox(
                  width: constraints.maxWidth > 900
                      ? 850
                      : constraints.maxWidth,
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      // HEADER
                      const Text(
                        'AI Food Business Analysis',
                        textAlign: TextAlign.center,
                        style: TextStyle(
                          fontSize: 24,
                          fontWeight: FontWeight.bold,
                        ),
                      ),

                      const SizedBox(height: 4),

                      Text(
                        'AI-powered business location evaluation',
                        textAlign: TextAlign.center,
                        style: TextStyle(
                          fontSize: 13,
                          color: Colors.grey.shade600,
                        ),
                      ),

                      const SizedBox(height: 16),

                      // MAIN SCORE
                      _buildMainScore(),

                      const SizedBox(height: 12),

                      // BUSINESS SCORES
                      _buildScores(),

                      const SizedBox(height: 12),

                      // DECISION
                      _buildDecision(),

                      const SizedBox(height: 12),

                      // RECOMMENDATION
                      _buildRecommendation(),

                      const SizedBox(height: 16),

                      // NEW PREDICTION
                      SizedBox(
                        height: 42,
                        child: OutlinedButton.icon(
                          onPressed: () {
                            Navigator.pop(context);
                          },
                          icon: const Icon(
                            Icons.refresh,
                            size: 18,
                          ),
                          label: const Text(
                            'New Prediction',
                            style: TextStyle(
                              fontWeight: FontWeight.w600,
                            ),
                          ),
                        ),
                      ),

                      const SizedBox(height: 12),
                    ],
                  ),
                ),
              ),
            );
          },
        ),
      ),
    );
  }

  // ============================================================
  // MAIN SCORE
  // ============================================================

  Widget _buildMainScore() {
    return Card(
      elevation: 2,
      child: Padding(
        padding: const EdgeInsets.symmetric(
          vertical: 18,
          horizontal: 20,
        ),
        child: Column(
          children: [
            Text(
              'Success Probability',
              style: TextStyle(
                fontSize: 14,
                color: Colors.grey.shade700,
                fontWeight: FontWeight.w500,
              ),
            ),

            const SizedBox(height: 4),

            Text(
              '${result.successProbability.toStringAsFixed(1)}%',
              style: const TextStyle(
                fontSize: 38,
                fontWeight: FontWeight.bold,
              ),
            ),

            const SizedBox(height: 4),

            Text(
              'Grade ${result.grade}',
              style: const TextStyle(
                fontSize: 17,
                fontWeight: FontWeight.bold,
              ),
            ),

            const SizedBox(height: 2),

            Text(
              result.overallStatus,
              style: TextStyle(
                fontSize: 13,
                color: Colors.grey.shade700,
              ),
            ),
          ],
        ),
      ),
    );
  }

  // ============================================================
  // SCORES
  // ============================================================

  Widget _buildScores() {
    return Card(
      elevation: 2,
      child: Padding(
        padding: const EdgeInsets.all(14),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              'Business Scores',
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.bold,
              ),
            ),

            const SizedBox(height: 10),

            Row(
              children: [
                Expanded(
                  child: _scoreBox(
                    'Business Score',
                    result.businessScore,
                  ),
                ),
                const SizedBox(width: 10),
                Expanded(
                  child: _scoreBox(
                    'AI Score',
                    result.overallAiScore,
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _scoreBox(
    String title,
    double value,
  ) {
    return Container(
      padding: const EdgeInsets.symmetric(
        vertical: 12,
        horizontal: 8,
      ),
      decoration: BoxDecoration(
        border: Border.all(
          color: Colors.grey.shade300,
        ),
        borderRadius: BorderRadius.circular(8),
      ),
      child: Column(
        children: [
          Text(
            title,
            textAlign: TextAlign.center,
            style: TextStyle(
              fontSize: 11,
              color: Colors.grey.shade600,
            ),
          ),

          const SizedBox(height: 4),

          Text(
            value.toStringAsFixed(2),
            style: const TextStyle(
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
          ),
        ],
      ),
    );
  }

  // ============================================================
  // DECISION
  // ============================================================

  Widget _buildDecision() {
    return Card(
      elevation: 2,
      child: Padding(
        padding: const EdgeInsets.all(14),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              'Investment Decision',
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.bold,
              ),
            ),

            const SizedBox(height: 8),

            _infoRow(
              'Decision',
              result.decision,
            ),

            _infoRow(
              'Confidence',
              result.confidence,
            ),

            _infoRow(
              'Risk Level',
              result.riskLevel,
            ),

            _infoRow(
              'Status',
              result.overallStatus,
            ),

            _infoRow(
              'Grade',
              result.grade,
            ),
          ],
        ),
      ),
    );
  }

  // ============================================================
  // RECOMMENDATION
  // ============================================================

  Widget _buildRecommendation() {
    return Card(
      elevation: 2,
      child: Padding(
        padding: const EdgeInsets.all(14),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              'AI Recommendation',
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.bold,
              ),
            ),

            const SizedBox(height: 8),

            Text(
              result.recommendation,
              style: const TextStyle(
                fontSize: 14,
                fontWeight: FontWeight.w500,
              ),
            ),
          ],
        ),
      ),
    );
  }

  // ============================================================
  // INFO ROW
  // ============================================================

  Widget _infoRow(
    String title,
    String value,
  ) {
    return Padding(
      padding: const EdgeInsets.symmetric(
        vertical: 4,
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Expanded(
            flex: 2,
            child: Text(
              title,
              style: const TextStyle(
                fontSize: 12,
                fontWeight: FontWeight.w500,
              ),
            ),
          ),

          const SizedBox(width: 12),

          Expanded(
            flex: 3,
            child: Text(
              value,
              textAlign: TextAlign.right,
              style: const TextStyle(
                fontSize: 12,
              ),
            ),
          ),
        ],
      ),
    );
  }
}