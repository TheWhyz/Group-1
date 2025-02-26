#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <climits>
#include <list>
#include <optional>
#include <algorithm>

using namespace std;

class Graph {
public:
    using RoadMap = unordered_map<string, vector<pair<string, int>>>; 
    RoadMap roads;

    void addRoad(string_view from, string_view to, int distance) {
        roads[string(from)].emplace_back(string(to), distance);
        roads[string(to)].emplace_back(string(from), distance);
    }

    void displayMap() const {
        cout << "\nCity Road Map:\n";
        for (const auto& [intersection, neighbors] : roads) {
            cout << intersection << " -> ";
            for (const auto& [neighbor, distance] : neighbors) {
                cout << "[" << neighbor << " (" << distance << " km)] ";
            }
            cout << '\n';
        }
    }

    optional<vector<string>> findShortestPath(string_view start, string_view destination) {
        if (roads.find(start.data()) == roads.end() || roads.find(destination.data()) == roads.end()) {
            cout << "Error: One or both intersections do not exist.\n";
            return nullopt;
        }

        unordered_map<string, int> distances;
        unordered_map<string, string> previous;
        unordered_set<string> visited;
        priority_queue<pair<int, string>, vector<pair<int, string>>, greater<>> minHeap;

        for (const auto& [node, _] : roads) {
            distances[node] = INT_MAX;
        }
        distances[start.data()] = 0;
        minHeap.push({0, string(start)});

        while (!minHeap.empty()) {
            auto [currentDistance, current] = minHeap.top();
            minHeap.pop();

            if (visited.find(current) != visited.end()) continue;
            visited.insert(current);

            if (current == destination) break;

            for (const auto& [neighbor, weight] : roads[current]) {
                int newDistance = currentDistance + weight;
                if (newDistance < distances[neighbor]) {
                    distances[neighbor] = newDistance;
                    previous[neighbor] = current;
                    minHeap.push({newDistance, neighbor});
                }
            }
        }

        if (distances[destination.data()] == INT_MAX) {
            cout << "No path found from " << start << " to " << destination << ".\n";
            return nullopt;
        }

        vector<string> path;
        for (string at = destination.data(); at != start.data(); at = previous[at]) {
            path.push_back(at);
        }
        path.push_back(start.data());
        reverse(path.begin(), path.end());

        return path;
    }
};

int main() {
    Graph cityMap;

    cityMap.addRoad("A", "B", 4);
    cityMap.addRoad("A", "C", 2);
    cityMap.addRoad("B", "C", 5);
    cityMap.addRoad("B", "D", 10);
    cityMap.addRoad("C", "D", 3);
    cityMap.addRoad("D", "E", 8);
    cityMap.addRoad("E", "F", 6);
    cityMap.addRoad("C", "F", 7);
    cityMap.addRoad("A", "F", 9);

    cityMap.displayMap();

    string start, destination;
    cout << "\nEnter start intersection: ";
    cin >> start;
    cout << "Enter destination intersection: ";
    cin >> destination;

    auto path = cityMap.findShortestPath(start, destination);
    if (path) {
        cout << "\nShortest Path: ";
        for (size_t i = 0; i < path->size(); ++i) {
            cout << (*path)[i] << (i + 1 < path->size() ? " -> " : "");
        }
        cout << " (Total Distance: " << cityMap.findShortestPath(start, destination).value().size() - 1 << " km)\n";
    }

    return 0;
}
