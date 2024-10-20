import traci

class prototype1:
    """
    Classe du prototype1 de gestion de feux de circulation avec SUMO et TraCI.
    """

    def __init__(self) -> None:
        """
        :attributs:
            traffic_light_id (str): ID du feu de circulation (ex. "J6").
            detectors (list[str]): Liste des ID des détecteurs inductifs (ex. ["e1_0", "e1_1"]).
        """
        # Démarrer SUMO_prototype1
        self.sumoCmd            = ["sumo-gui", "-c", "SUMO_prototype1/sumo_prototype1_test.sumocfg"]

        # Setup des id
        self.traffic_light_id   = "J6"                              # ID de notre feu
        self.detectors          = ["e1_0", "e1_1", "e1_2", "e1_3"]  # ID detecteur

# Fonction pour lire les données des capteurs
    def check_inductive_loops(self) -> str | None:
        """
        Vérifie les boucles inductives et renvoie l'identifiant du détecteur qui a détecté
        des véhicules lors de la dernière étape de simulation.

        :return: L'ID du détecteur ayant détecté des véhicules ou None si aucun véhicule
                 n'a été détecté.
        """

        print('\n')
        for detector_id in self.detectors:
            # Obtenir le nombre de véhicules détectés depuis la dernière étape
            detected_vehicles = traci.inductionloop.getLastStepVehicleNumber(detector_id)

            if detected_vehicles > 0:
                return detector_id

        return None
    
    def launch(self):
        """
        Démarre la simulation SUMO avec la commande spécifiée.
        
        :return: None
        """
        traci.start(self.sumoCmd)


if __name__ == '__main__':
    prototype1()