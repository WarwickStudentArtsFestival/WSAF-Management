import 'config/base.just'

project_slug := 'wsaf-management'

# List available commands
@_default:
    just -l

# Upgrade both Python and Node
@upgrade_all_packages:
    # kill all running containers
    docker stop $(docker ps -a -q) || true
    # remove all stopped containers
    docker rm $(docker ps -a -q) || true
    just upgrade_python_packages
    just upgrade_node_packages
    just build
    just pre_commit
