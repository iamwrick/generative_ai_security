import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

G.add_node("Generative AI Client")
G.add_node("Secure Encrypted Data")
G.add_node("Generative AI Server")

G.add_edge("Generative AI Client", "Secure Encrypted Data", label="Send Encrypted Data")
G.add_edge("Secure Encrypted Data", "Generative AI Server", label="Receive Encrypted Data")

plt.figure(figsize=(10, 6))
pos = {
    "Generative AI Client": (0, 1),
    "Secure Encrypted Data": (1, 0.5),
    "Generative AI Server": (2, 1),
}

nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold', arrowsize=20)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

plt.savefig('tls_communication_flow.png', dpi=300)
plt.title("Generative AI TLS Communication Flow")
plt.show()
