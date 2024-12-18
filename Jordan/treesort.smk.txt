rule treesort:
    message: "running treesort to infer reassortment events"
    input:
        descriptor = files.treesort_descriptor,
        trees = expand("results/tree_{subtype}_{segment}_pruned.nwk", subtype=SUBTYPES, segment=SEGMENTS)
    output:
        tree = "treesort/ha_treesort.tre"
    run:
        commands = [
            "pip install git+https://github.com/flu-crew/TreeSort",
            """
            treesort \
            -i {input.descriptor} \
            -o {output.tree}
            """
        ]
        for c in commands:
            shell(c)