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
      appBar: AppBar(
        title: const Text('Business Prediction Result'),
        centerTitle: true,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 1000),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                const Text(
                  'AI Business Analysis',
                  style: TextStyle(
                    fontSize: 30,
                    fontWeight: FontWeight.bold,
                  ),
                  textAlign: TextAlign.center,
                ),

                const SizedBox(height: 8),

                Text(
                  result.decision,
                  style: const TextStyle(
                    fontSize: 20,
                  ),
                  textAlign: TextAlign.center,
                ),

                const SizedBox(height: 25),

                _scoreCard(),

                const SizedBox(height: 20),

                _detailsCard(),

                const SizedBox(height: 20),

                _analyticsCard(),

                const SizedBox(height: 20),

                _additionalAnalysisCard(),

                const SizedBox(height: 30),

                ElevatedButton.icon(
                  onPressed: () {
                    Navigator.pop(context);
                  },
                  icon: const Icon(Icons.refresh),
                  label: const Text(
                    'New Prediction',
                    style: TextStyle(fontSize: 16),
                  ),
                  style: ElevatedButton.styleFrom(
                    padding: const EdgeInsets.symmetric(
                      vertical: 16,
                    ),
                  ),
                ),

                const SizedBox(height: 20),
              ],
            ),
          ),
        ),
      ),
    );
  }

  // ============================================================
  // SCORE CARD
  // ============================================================

  Widget _scoreCard() {
    return Card(
      elevation: 5,
      child: Padding(
        padding: const EdgeInsets.all(30),
        child: Column(
          children: [
            const Text(
              'Success Probability',
              style: TextStyle(
                fontSize: 20,
                fontWeight: FontWeight.w600,
              ),
            ),

            const SizedBox(height: 15),

            Text(
              '${result.successProbability.toStringAsFixed(2)}%',
              style: const TextStyle(
                fontSize: 46,
                fontWeight: FontWeight.bold,
              ),
            ),

            const SizedBox(height: 10),

            Text(
              'Grade ${result.grade}',
              style: const TextStyle(
                fontSize: 24,
                fontWeight: FontWeight.bold,
              ),
            ),

            const SizedBox(height: 15),

            Text(
              result.overallStatus,
              style: const TextStyle(
                fontSize: 18,
              ),
            ),
          ],
        ),
      ),
    );
  }

  // ============================================================
  // BASIC BUSINESS ANALYSIS
  // ============================================================

  Widget _detailsCard() {
    return _sectionCard(
      title: 'Business Analysis',
      icon: Icons.business,
      children: [
        _row(
          'Business Score',
          result.businessScore.toStringAsFixed(2),
        ),
        _row(
          'Overall AI Score',
          result.overallAiScore.toStringAsFixed(2),
        ),
        _row(
          'Overall Status',
          result.overallStatus,
        ),
        _row(
          'Decision',
          result.decision,
        ),
        _row(
          'Confidence',
          result.confidence,
        ),
        _row(
          'Risk Level',
          result.riskLevel,
        ),
        _row(
          'Recommendation',
          result.recommendation,
        ),
      ],
    );
  }

  // ============================================================
  // ANALYTICS
  // ============================================================

  Widget _analyticsCard() {
    final analytics = result.analytics;

    return _sectionCard(
      title: 'Market & Location Analytics',
      icon: Icons.analytics,
      children: [
        _analyticsRow(
          'Business Health Index',
          analytics['business_health_index'],
        ),
        _analyticsRow(
          'Location Quality Index',
          analytics['location_quality_index'],
        ),
        _analyticsRow(
          'Demand Score',
          analytics['demand_score'],
        ),
        _analyticsRow(
          'Competition Score',
          analytics['competition_score'],
        ),
        _analyticsRow(
          'Affordability Score',
          analytics['affordability_score'],
        ),
        _analyticsRow(
          'Growth Score',
          analytics['growth_score'],
        ),
        _analyticsRow(
          'Commercial Activity',
          analytics['commercial_activity_score'],
        ),
        _analyticsRow(
          'Market Attractiveness',
          analytics['market_attractiveness'],
        ),
        _analyticsRow(
          'Risk Index',
          analytics['risk_index'],
        ),
        _textRow(
          'Opportunity Level',
          analytics['opportunity_level'],
        ),
        _textRow(
          'Business Readiness',
          analytics['business_readiness'],
        ),
        _textRow(
          'Investment Category',
          analytics['investment_category'],
        ),
      ],
    );
  }

  // ============================================================
  // ADDITIONAL ANALYSIS
  // ============================================================

  Widget _additionalAnalysisCard() {
    final sections = <Widget>[];

    _addMapSection(
      sections,
      'Customer Analysis',
      Icons.people,
      result.customerAnalysis,
    );

    _addMapSection(
      sections,
      'SWOT Analysis',
      Icons.balance,
      result.swotAnalysis,
    );

    _addMapSection(
      sections,
      'Investment Analysis',
      Icons.account_balance,
      result.investmentAnalysis,
    );

    _addMapSection(
      sections,
      'ROI Analysis',
      Icons.trending_up,
      result.roiAnalysis,
    );

    _addMapSection(
      sections,
      'Business Performance',
      Icons.speed,
      result.businessPerformance,
    );

    _addMapSection(
      sections,
      'Business Recommendations',
      Icons.lightbulb,
      result.businessRecommendations,
    );

    _addMapSection(
      sections,
      'Executive Report',
      Icons.description,
      result.executiveReport,
    );

    if (sections.isEmpty) {
      return const SizedBox.shrink();
    }

    return Card(
      elevation: 4,
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: sections,
        ),
      ),
    );
  }

  void _addMapSection(
    List<Widget> sections,
    String title,
    IconData icon,
    Map<String, dynamic> data,
  ) {
    if (data.isEmpty) {
      return;
    }

    sections.add(
      Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(icon),
              const SizedBox(width: 10),
              Text(
                title,
                style: const TextStyle(
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ],
          ),

          const SizedBox(height: 12),

          ...data.entries.map(
            (entry) => _dynamicRow(
              _formatLabel(entry.key),
              entry.value,
            ),
          ),

          const SizedBox(height: 20),
        ],
      ),
    );
  }

  // ============================================================
  // COMMON SECTION CARD
  // ============================================================

  Widget _sectionCard({
    required String title,
    required IconData icon,
    required List<Widget> children,
  }) {
    return Card(
      elevation: 4,
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Icon(icon),
                const SizedBox(width: 10),
                Text(
                  title,
                  style: const TextStyle(
                    fontSize: 22,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ],
            ),

            const SizedBox(height: 20),

            ...children,
          ],
        ),
      ),
    );
  }

  // ============================================================
  // ROW
  // ============================================================

  Widget _row(
    String title,
    String value,
  ) {
    return Padding(
      padding: const EdgeInsets.symmetric(
        vertical: 9,
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Expanded(
            child: Text(
              title,
              style: const TextStyle(
                fontWeight: FontWeight.w600,
              ),
            ),
          ),
          const SizedBox(width: 20),
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

  // ============================================================
  // ANALYTICS NUMBER ROW
  // ============================================================

  Widget _analyticsRow(
    String title,
    dynamic value,
  ) {
    if (value == null) {
      return const SizedBox.shrink();
    }

    String displayValue;

    if (value is num) {
      displayValue = value.toStringAsFixed(2);
    } else {
      displayValue = value.toString();
    }

    return _row(
      title,
      displayValue,
    );
  }

  // ============================================================
  // TEXT ROW
  // ============================================================

  Widget _textRow(
    String title,
    dynamic value,
  ) {
    if (value == null) {
      return const SizedBox.shrink();
    }

    return _row(
      title,
      value.toString(),
    );
  }

  // ============================================================
  // DYNAMIC ROW
  // ============================================================

  Widget _dynamicRow(
    String title,
    dynamic value,
  ) {
    if (value == null) {
      return const SizedBox.shrink();
    }

    if (value is Map) {
      return Padding(
        padding: const EdgeInsets.symmetric(
          vertical: 6,
        ),
        child: ExpansionTile(
          title: Text(
            title,
            style: const TextStyle(
              fontWeight: FontWeight.w600,
            ),
          ),
          children: value.entries.map<Widget>(
            (entry) {
              return _dynamicRow(
                _formatLabel(entry.key.toString()),
                entry.value,
              );
            },
          ).toList(),
        ),
      );
    }

    if (value is List) {
      return Padding(
        padding: const EdgeInsets.symmetric(
          vertical: 6,
        ),
        child: Column(
          crossAxisAlignment:
              CrossAxisAlignment.start,
          children: [
            Text(
              title,
              style: const TextStyle(
                fontWeight: FontWeight.w600,
              ),
            ),
            const SizedBox(height: 5),
            ...value.map(
              (item) => Padding(
                padding: const EdgeInsets.only(
                  left: 15,
                  bottom: 4,
                ),
                child: Text(
                  '• ${item.toString()}',
                ),
              ),
            ),
          ],
        ),
      );
    }

    String displayValue;

    if (value is num) {
      displayValue = value.toStringAsFixed(2);
    } else {
      displayValue = value.toString();
    }

    return _row(
      title,
      displayValue,
    );
  }

  // ============================================================
  // FORMAT LABEL
  // ============================================================

  String _formatLabel(String value) {
    return value
        .replaceAll('_', ' ')
        .split(' ')
        .map(
          (word) {
            if (word.isEmpty) {
              return word;
            }

            return word[0].toUpperCase() +
                word.substring(1);
          },
        )
        .join(' ');
  }
}