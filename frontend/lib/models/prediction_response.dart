class PredictionResponse {
  final int prediction;
  final double successProbability;
  final double businessScore;
  final double overallAiScore;
  final String overallStatus;
  final String grade;
  final String decision;
  final String confidence;
  final String riskLevel;
  final String recommendation;

  final Map<String, dynamic> analytics;
  final Map<String, dynamic> dashboard;
  final Map<String, dynamic> customerAnalysis;
  final Map<String, dynamic> swotAnalysis;
  final Map<String, dynamic> investmentAnalysis;
  final Map<String, dynamic> roiAnalysis;
  final Map<String, dynamic> businessPerformance;
  final Map<String, dynamic> businessRecommendations;
  final Map<String, dynamic> executiveReport;

  PredictionResponse({
    required this.prediction,
    required this.successProbability,
    required this.businessScore,
    required this.overallAiScore,
    required this.overallStatus,
    required this.grade,
    required this.decision,
    required this.confidence,
    required this.riskLevel,
    required this.recommendation,
    required this.analytics,
    required this.dashboard,
    required this.customerAnalysis,
    required this.swotAnalysis,
    required this.investmentAnalysis,
    required this.roiAnalysis,
    required this.businessPerformance,
    required this.businessRecommendations,
    required this.executiveReport,
  });

  factory PredictionResponse.fromJson(
    Map<String, dynamic> json,
  ) {
    return PredictionResponse(
      prediction:
          (json['prediction'] as num?)?.toInt() ?? 0,

      successProbability:
          (json['success_probability'] as num?)
                  ?.toDouble() ??
              0.0,

      businessScore:
          (json['business_score'] as num?)
                  ?.toDouble() ??
              0.0,

      overallAiScore:
          (json['overall_ai_score'] as num?)
                  ?.toDouble() ??
              0.0,

      overallStatus:
          json['overall_status']?.toString() ?? '',

      grade:
          json['grade']?.toString() ?? '',

      decision:
          json['decision']?.toString() ?? '',

      confidence:
          json['confidence']?.toString() ?? '',

      riskLevel:
          json['risk_level']?.toString() ?? '',

      recommendation:
          json['recommendation']?.toString() ?? '',

      analytics:
          Map<String, dynamic>.from(
        json['analytics'] ?? {},
      ),

      dashboard:
          Map<String, dynamic>.from(
        json['dashboard'] ?? {},
      ),

      customerAnalysis:
          Map<String, dynamic>.from(
        json['customer_analysis'] ?? {},
      ),

      swotAnalysis:
          Map<String, dynamic>.from(
        json['swot_analysis'] ?? {},
      ),

      investmentAnalysis:
          Map<String, dynamic>.from(
        json['investment_analysis'] ?? {},
      ),

      roiAnalysis:
          Map<String, dynamic>.from(
        json['roi_analysis'] ?? {},
      ),

      businessPerformance:
          Map<String, dynamic>.from(
        json['business_performance'] ?? {},
      ),

      businessRecommendations:
          Map<String, dynamic>.from(
        json['business_recommendations'] ?? {},
      ),

      executiveReport:
          Map<String, dynamic>.from(
        json['executive_report'] ?? {},
      ),
    );
  }
}