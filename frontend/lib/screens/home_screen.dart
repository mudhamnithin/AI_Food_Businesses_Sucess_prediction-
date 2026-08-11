import 'package:flutter/material.dart';

import '../models/prediction_request.dart';
import '../models/prediction_response.dart';
import '../services/prediction_service.dart';
import '../widgets/input_field.dart';
import 'result_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final _formKey = GlobalKey<FormState>();

  final avgIncomeController = TextEditingController();
  final distanceController = TextEditingController();
  final footfallController = TextEditingController();
  final collegesController = TextEditingController();
  final hospitalsController = TextEditingController();
  final officesController = TextEditingController();
  final parksController = TextEditingController();
  final restaurantsController = TextEditingController();
  final shopsController = TextEditingController();
  final rentController = TextEditingController();

  final PredictionService predictionService = PredictionService();

  bool isLoading = false;
  String? errorMessage;

  Future<void> predictBusiness() async {
    if (!_formKey.currentState!.validate()) {
      return;
    }

    setState(() {
      isLoading = true;
      errorMessage = null;
    });

    try {
      final request = PredictionRequest(
        avgIncomeArea: double.parse(avgIncomeController.text),
        distanceToNearestBrandChai:
            double.parse(distanceController.text),
        footfallIndex: double.parse(footfallController.text),
        nearbyCollegesCount:
            double.parse(collegesController.text),
        nearbyHospitalsCount:
            double.parse(hospitalsController.text),
        nearbyOfficesCount:
            double.parse(officesController.text),
        nearbyParksCount:
            double.parse(parksController.text),
        nearbyRestaurantsCount:
            double.parse(restaurantsController.text),
        nearbyShopsCount:
            double.parse(shopsController.text),
        rentEstimate: double.parse(rentController.text),
      );

      final PredictionResponse prediction =
          await predictionService.predict(request);

      if (!mounted) return;

      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => ResultScreen(
            result: prediction,
          ),
        ),
      );
    } catch (e) {
      if (!mounted) return;

      setState(() {
        errorMessage = e.toString();
      });
    } finally {
      if (mounted) {
        setState(() {
          isLoading = false;
        });
      }
    }
  }

  @override
  void dispose() {
    avgIncomeController.dispose();
    distanceController.dispose();
    footfallController.dispose();
    collegesController.dispose();
    hospitalsController.dispose();
    officesController.dispose();
    parksController.dispose();
    restaurantsController.dispose();
    shopsController.dispose();
    rentController.dispose();

    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Food Business Prediction',
        ),
        centerTitle: true,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Form(
          key: _formKey,
          child: Center(
            child: ConstrainedBox(
              constraints: const BoxConstraints(
                maxWidth: 900,
              ),
              child: Column(
                crossAxisAlignment:
                    CrossAxisAlignment.stretch,
                children: [
                  const Text(
                    'AI-Powered Food Business Success Prediction',
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      fontSize: 28,
                      fontWeight: FontWeight.bold,
                    ),
                  ),

                  const SizedBox(height: 30),

                  InputField(
                    label: 'Average Income Area',
                    hint: 'Example: 35',
                    controller: avgIncomeController,
                  ),

                  const SizedBox(height: 15),

                  InputField(
                    label:
                        'Distance To Nearest Brand Chai',
                    hint: 'Example: 1200',
                    controller: distanceController,
                  ),

                  const SizedBox(height: 15),

                  InputField(
                    label: 'Footfall Index',
                    hint: 'Example: 95',
                    controller: footfallController,
                  ),

                  const SizedBox(height: 15),

                  InputField(
                    label: 'Nearby Colleges Count',
                    hint: 'Example: 8',
                    controller: collegesController,
                  ),

                  const SizedBox(height: 15),

                  InputField(
                    label: 'Nearby Hospitals Count',
                    hint: 'Example: 5',
                    controller: hospitalsController,
                  ),

                  const SizedBox(height: 15),

                  InputField(
                    label: 'Nearby Offices Count',
                    hint: 'Example: 35',
                    controller: officesController,
                  ),

                  const SizedBox(height: 15),

                  InputField(
                    label: 'Nearby Parks Count',
                    hint: 'Example: 4',
                    controller: parksController,
                  ),

                  const SizedBox(height: 15),

                  InputField(
                    label:
                        'Nearby Restaurants Count',
                    hint: 'Example: 5',
                    controller: restaurantsController,
                  ),

                  const SizedBox(height: 15),

                  InputField(
                    label: 'Nearby Shops Count',
                    hint: 'Example: 25',
                    controller: shopsController,
                  ),

                  const SizedBox(height: 15),

                  InputField(
                    label: 'Rent Estimate',
                    hint: 'Example: 30',
                    controller: rentController,
                  ),

                  const SizedBox(height: 25),

                  ElevatedButton(
                    onPressed:
                        isLoading ? null : predictBusiness,
                    style: ElevatedButton.styleFrom(
                      padding:
                          const EdgeInsets.symmetric(
                        vertical: 16,
                      ),
                    ),
                    child: isLoading
                        ? const SizedBox(
                            height: 22,
                            width: 22,
                            child:
                                CircularProgressIndicator(),
                          )
                        : const Text(
                            'Predict Business Success',
                            style: TextStyle(
                              fontSize: 16,
                            ),
                          ),
                  ),

                  const SizedBox(height: 25),

                  if (errorMessage != null)
                    Card(
                      child: Padding(
                        padding:
                            const EdgeInsets.all(16),
                        child: Text(
                          errorMessage!,
                          style: const TextStyle(
                            color: Colors.red,
                          ),
                        ),
                      ),
                    ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}