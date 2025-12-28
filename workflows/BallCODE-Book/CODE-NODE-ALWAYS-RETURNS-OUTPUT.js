// Code Node for Clone/Update Repository
// This version ALWAYS returns output, even on errors

// Get data from previous node
const data = $input.item.json || {};

// Extract values with fallbacks
const repoUrl = data.repoUrl || data.UNITY_REPO_URL || '';
const projectPath = data.projectPath || data.UNITY_PROJECT_PATH || '';

// Log everything for debugging
console.log('=== Clone/Update Repository Debug ===');
console.log('Input data:', JSON.stringify(data, null, 2));
console.log('repoUrl:', repoUrl);
console.log('projectPath:', projectPath);

// ALWAYS return something - even if validation fails
if (!repoUrl || repoUrl.trim() === '') {
  console.error('ERROR: repoUrl is empty');
  return {
    json: {
      success: false,
      error: 'repoUrl is empty or not set',
      action: 'skipped',
      message: 'UNITY_REPO_URL is missing. Check previous node output.',
      debug: {
        repoUrl: repoUrl,
        projectPath: projectPath,
        inputData: data
      }
    }
  };
}

if (!projectPath || projectPath.trim() === '') {
  console.error('ERROR: projectPath is empty');
  return {
    json: {
      success: false,
      error: 'projectPath is empty or not set',
      action: 'skipped',
      message: 'UNITY_PROJECT_PATH is missing. Check previous node output.',
      debug: {
        repoUrl: repoUrl,
        projectPath: projectPath,
        inputData: data
      }
    }
  };
}

// Try to execute git command
// Use try-catch to ensure we ALWAYS return something
try {
  console.log('Attempting git operation...');
  console.log('repoUrl:', repoUrl);
  console.log('projectPath:', projectPath);
  
  // Check if $exec is available
  if (typeof $exec === 'undefined') {
    console.error('$exec is not available');
    return {
      json: {
        success: false,
        error: '$exec() function is not available in this n8n version',
        action: 'error',
        message: 'This n8n version does not support $exec(). Use executeCommand node instead.',
        repoUrl: repoUrl,
        projectPath: projectPath,
        suggestion: 'Replace this Code node with an executeCommand node'
      }
    };
  }
  
  // Check if directory exists
  const checkCmd = `test -d "${projectPath}" && echo "exists" || echo "not_exists"`;
  console.log('Running check command:', checkCmd);
  
  const checkResult = $exec(checkCmd);
  console.log('Check result:', checkResult);
  console.log('Check stdout:', checkResult.stdout);
  console.log('Check exitCode:', checkResult.exitCode);
  
  const dirExists = checkResult.stdout && checkResult.stdout.trim() === 'exists';
  console.log('Directory exists?', dirExists);
  
  if (dirExists) {
    // Directory exists - do git pull
    console.log('Directory exists - running git pull...');
    const pullCmd = `cd "${projectPath}" && git pull`;
    console.log('Pull command:', pullCmd);
    
    const pullResult = $exec(pullCmd);
    console.log('Pull result:', pullResult);
    console.log('Pull stdout:', pullResult.stdout);
    console.log('Pull stderr:', pullResult.stderr);
    console.log('Pull exitCode:', pullResult.exitCode);
    
    return {
      json: {
        success: pullResult.exitCode === 0,
        action: 'pulled',
        path: projectPath,
        message: pullResult.exitCode === 0 ? 'Git pull completed successfully' : 'Git pull failed',
        output: pullResult.stdout || '',
        error: pullResult.stderr || '',
        exitCode: pullResult.exitCode,
        command: pullCmd
      }
    };
  } else {
    // Directory doesn't exist - do git clone
    console.log('Directory does not exist - running git clone...');
    
    // Create parent directory first
    const pathParts = projectPath.split('/').filter(p => p);
    const parentDir = '/' + pathParts.slice(0, -1).join('/');
    console.log('Parent directory:', parentDir);
    
    if (parentDir && parentDir !== '/') {
      const mkdirCmd = `mkdir -p "${parentDir}"`;
      console.log('Creating parent directory:', mkdirCmd);
      const mkdirResult = $exec(mkdirCmd);
      console.log('Mkdir result:', mkdirResult);
    }
    
    // Now clone
    const cloneCmd = `git clone "${repoUrl}" "${projectPath}"`;
    console.log('Clone command:', cloneCmd);
    
    const cloneResult = $exec(cloneCmd);
    console.log('Clone result:', cloneResult);
    console.log('Clone stdout:', cloneResult.stdout);
    console.log('Clone stderr:', cloneResult.stderr);
    console.log('Clone exitCode:', cloneResult.exitCode);
    
    return {
      json: {
        success: cloneResult.exitCode === 0,
        action: 'cloned',
        path: projectPath,
        message: cloneResult.exitCode === 0 ? 'Git clone completed successfully' : 'Git clone failed',
        output: cloneResult.stdout || '',
        error: cloneResult.stderr || '',
        exitCode: cloneResult.exitCode,
        command: cloneCmd
      }
    };
  }
} catch (error) {
  // ALWAYS return error details
  console.error('Exception caught:', error);
  console.error('Error message:', error.message);
  console.error('Error stack:', error.stack);
  
  return {
    json: {
      success: false,
      error: error.message || 'Unknown error occurred',
      errorType: error.name || 'Error',
      action: 'error',
      message: 'An exception occurred while executing git operation',
      stack: error.stack || '',
      repoUrl: repoUrl,
      projectPath: projectPath,
      debug: {
        errorName: error.name,
        errorMessage: error.message,
        errorStack: error.stack
      }
    }
  };
}


