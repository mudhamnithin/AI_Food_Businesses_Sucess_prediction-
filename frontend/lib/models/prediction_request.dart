class PredictionRequest {
  final double avgIncomeArea;
  final double distanceToNearestBrandChai;
  final double footfallIndex;
  final double nearbyCollegesCount;
  final double nearbyHospitalsCount;
  final double nearbyOfficesCount;
  final double nearbyParksCount;
  final double nearbyRestaurantsCount;
  final double nearbyShopsCount;
  final double rentEstimate;

  PredictionRequest({
    required this.avgIncomeArea,
    required this.distanceToNearestBrandChai,
    required this.footfallIndex,
    required this.nearbyCollegesCount,
    required this.nearbyHospitalsCount,
    required this.nearbyOfficesCount,
    required this.nearbyParksCount,
    required this.nearbyRestaurantsCount,
    required this.nearbyShopsCount,
    required this.rentEstimate,
  });

  Map<String, dynamic> toJson() {
    return {
      'avg_income_area': avgIncomeArea,
      'distance_to_nearest_brand_chai': distanceToNearestBrandChai,
      'footfall_index': footfallIndex,
      'nearby_colleges_count': nearbyCollegesCount,
      'nearby_hospitals_count': nearbyHospitalsCount,
      'nearby_offices_count': nearbyOfficesCount,
      'nearby_parks_count': nearbyParksCount,
      'nearby_restaurants_count': nearbyRestaurantsCount,
      'nearby_shops_count': nearbyShopsCount,
      'rent_estimate': rentEstimate,
    };
  }
}