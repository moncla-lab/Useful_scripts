rule annotate_treesort:
    message: "converting treesort tree into a node data json"
    input:
        tree = rules.treesort.output.tree
    output:
        node_data = "treesort/treesort.json"
    shell:
        """
        python scripts/annotate_treesort.py \
        --treesort_tree {input.tree} \
        --output {output.node_data}
        """