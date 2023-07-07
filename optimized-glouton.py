import csv
import time

start_time = time.time()

MAX_BUDGET = 500

def get_actions(fichier_csv):
    """
    Cette fonction permet de récupérer les données d'un fichier au format .csv.

    Args:
        fichier_csv (str): Nom du fichier au format .csv.

    Returns:
        actions (dict): Dictionnaire où chaque clé correspond au nom d'une action et chaque valeur est
        composée d'une liste [coût de l'action, profit (% du coût obtenu), profit (valeur brute)].
    """
    actions = {}
    try:
        with open(fichier_csv, newline='') as dataset:
            csv_reader = csv.reader(dataset)
            next(csv_reader)  # Ignorer la première ligne (en-tête)
            for count, row in enumerate(csv_reader):
                if len(row) == 3:
                    try:
                        cost = float(row[1])
                        profit_percentage = float(row[2])
                        if cost > 1:
                            value = cost * (profit_percentage / 100)
                            new_action = [cost, profit_percentage, round(value, 2)]
                            actions[row[0]] = new_action
                    except ValueError:
                        print(f"Erreur de conversion des valeurs de la ligne {count + 1}.")
                else:
                    print(f"Format incorrect pour la ligne {count + 1}.")
    except FileNotFoundError:
        print("Le fichier CSV spécifié est introuvable.")
    except Exception as e:
        print("Une erreur s'est produite lors de la lecture du fichier CSV :", str(e))

    return actions


def sort_actions_by_profit_percentage(actions):
    """
    Cette fonction permet de trier les actions par pourcentage de profit décroissant.

    Args:
        actions (dict): Dictionnaire des actions.

    Returns:
        sorted_actions (dict): Dictionnaire des actions triées par pourcentage de profit décroissant.
    """
    sorted_actions = {action_name: dict_value for action_name, dict_value in sorted(actions.items(),
                                                                                    key=lambda item: item[1][1],
                                                                                    reverse=True)}
    return sorted_actions


def get_invest(sorted_actions):
    """
    Cette fonction sélectionne les actions les plus rentables jusqu'à ce que le coût total atteigne le budget maximum.

    Args:
        sorted_actions (dict): Dictionnaire des actions triées par pourcentage de profit décroissant.

    Returns:
        invest (list): Liste des actions recommandées, coût total d'investissement et bénéfice total d'investissement.
    """
    list_of_actions = []
    cost = 0
    value = 0
    for item in sorted_actions.items():
        cost_of_item = item[1][0]
        testing_cost = cost + cost_of_item
        if testing_cost <= MAX_BUDGET:
            list_of_actions.append(item[0])
            cost = testing_cost
            value += item[1][2]
    invest = [list_of_actions, round(cost, 2), round(value, 2)]
    return invest


def print_information(invest):
    """
    Cette fonction affiche les informations sur l'investissement recommandé.

    Args:
        invest (list): Liste des actions recommandées, coût total d'investissement et bénéfice total d'investissement.
    """
    print("Vous devriez investir dans les actions suivantes :")
    for action in invest[0]:
        print(action)
    print("\nCela vous coûtera " + str(invest[1]) + "€.")
    print("Vous recevrez " + str(invest[2]) + "€ de bénéfice au bout de deux ans.")


def main():
    """
    Fonction principale pour exécuter le programme.
    """
    actions = get_actions('bruteforce_dataset.csv')
    sorted_actions = sort_actions_by_profit_percentage(actions)
    invest = get_invest(sorted_actions)
    print("--- %s seconds ---" % (time.time() - start_time))
    print_information(invest)


main()
