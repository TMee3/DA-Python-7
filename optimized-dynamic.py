import csv
import time

start_time = time.time()


def get_actions(fichier_csv):
    """
    Cette fonction permet de récupérer les données d'un fichier au format CSV.

    Args:
        fichier_csv (str): Nom du fichier CSV.

    Returns:
        list: Liste des actions, des prix et des bénéfices.
    """
    list_of_actions = []
    price = []
    profit = []

    try:
        with open(fichier_csv, newline='') as dataset:
            csv_reader = csv.reader(dataset)
            next(csv_reader)  # Ignorer la première ligne (en-tête)

            for count, row in enumerate(csv_reader):
                if len(row) == 3:
                    try:
                        profit_of_actions = int(round(float(row[1]) * float(row[2]) / 100, 2) * 100)
                        price_of_actions = int(float(row[1]) * 100)
                        list_of_actions.append(row[0])
                        price.append(price_of_actions)
                        profit.append(profit_of_actions)
                    except ValueError:
                        print(f"Erreur de conversion des valeurs de la ligne {count + 1}.")
                else:
                    print(f"Format incorrect pour la ligne {count + 1}.")
    except FileNotFoundError:
        print("Le fichier CSV spécifié est introuvable.")
    except Exception as e:
        print("Une erreur s'est produite lors de la lecture du fichier CSV :", str(e))

    actions = [list_of_actions, price, profit]
    return actions


def get_best_invest(actions, max_cost):
    """
    Cette fonction détermine l'investissement optimal en fonction des actions et du coût maximal.

    Args:
        actions (list): Liste des actions, des prix et des bénéfices.
        max_cost (int): Coût maximal d'investissement.

    Returns:
        list: Actions recommandées et bénéfice total.
    """
    list_of_actions = actions[0]
    price = actions[1]
    profit = actions[2]
    memory_actions = [[[] for cost in range(max_cost + 1)] for number_of_actions in range(len(list_of_actions) + 1)]
    memory_value = [[0 for cost in range(max_cost + 1)] for number_of_actions in range(len(list_of_actions) + 1)]

    try:
        for number_of_actions in range(1, len(list_of_actions) + 1):
            for cost in range(max_cost + 1):
                exclude_action = memory_value[number_of_actions - 1][cost]
                if price[number_of_actions - 1] > cost:
                    memory_value[number_of_actions][cost] = exclude_action
                    memory_actions[number_of_actions][cost] = memory_actions[number_of_actions - 1][cost]
                else:
                    include_action_base_price = cost - price[number_of_actions - 1]
                    if exclude_action > memory_value[number_of_actions - 1][include_action_base_price] + \
                            profit[number_of_actions - 1]:
                        memory_value[number_of_actions][cost] = exclude_action
                        memory_actions[number_of_actions][cost] = memory_actions[number_of_actions - 1][cost]
                    else:
                        memory_value[number_of_actions][cost] = \
                            memory_value[number_of_actions - 1][include_action_base_price] + \
                            profit[number_of_actions - 1]
                        memory_actions[number_of_actions][cost] = \
                            memory_actions[number_of_actions - 1][include_action_base_price] + \
                            [list_of_actions[number_of_actions - 1]]

        memory = [memory_actions[-1][-1], memory_value[-1][-1]]
        return memory
    except Exception as e:
        print("Une erreur s'est produite lors du calcul de l'investissement optimal :", str(e))


def print_information(invest, actions):
    """
    Cette fonction affiche les informations sur l'investissement recommandé.

    Args:
        invest (list): Actions recommandées et bénéfice total.
        actions (list): Liste des actions, des prix et des bénéfices.
    """
    if invest is None:
        print("Impossible de générer les informations d'investissement.")
        return

    print("Vous devriez investir dans les actions suivantes :")
    cost = 0
    for action_name in invest[0]:
        print(action_name)
        for index, action in enumerate(actions[0]):
            if action_name == action:
                cost = cost + actions[1][index]

    print("\nCela vous coûtera " + str(cost/100) + "€.")
    print("Vous recevrez " + str(invest[1]/100) + "€ de bénéfice au bout de deux ans.")


def main():
    """
    Fonction principale pour exécuter le programme.
    """
    actions = get_actions('bruteforce_dataset.csv')

    maxinvest = 500
    maxbudget = maxinvest * 100

    if actions:
        invest = get_best_invest(actions, maxbudget)
        print("--- %s seconds ---" % (time.time() - start_time))
        print_information(invest, actions)


main()
