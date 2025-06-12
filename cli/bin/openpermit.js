#!/usr/bin/env node

const { program } = require('commander');
const chalk = require('chalk');
const { version } = require('../package.json');

program
  .version(version)
  .description('OpenPermit CLI - Municipal permitting made simple');

program
  .command('init <project-name>')
  .description('Initialize new OpenPermit project')
  .action(require('../commands/init'));

program
  .command('generate <template>')
  .description('Generate permit template')
  .option('-t, --type <type>', 'permit type')
  .action(require('../commands/generate'));

program
  .command('demo <action>')
  .description('Demo environment management')
  .action(require('../commands/demo'));

program
  .command('config <action> [key] [value]')
  .description('Configuration management')
  .action(require('../commands/config'));

program
  .command('deploy')
  .description('Deploy to municipal environment')
  .option('-e, --env <environment>', 'deployment environment')
  .action(require('../commands/deploy'));

program.parse();
